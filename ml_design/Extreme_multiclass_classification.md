



You have hit on the exact reason why this is considered a highly advanced ML problem. When a single event causes multiple outputs (multiple parts) and your total list of possible parts is massive (hundreds, thousands, or even tens of thousands of OEM part numbers), standard multi-label classification breaks down. 

In machine learning, this is known as **Extreme Multi-Label Classification (XMC)**. If you use a standard neural network with a massive output layer (e.g., 10,000 nodes, one for each part), the model will struggle because 99% of the parts are *not* damaged in any given crash, leading to extreme data sparsity and dead gradients.

Here is how you architect a system to handle a huge, multi-part catalog effectively.

---

### 1. The Hierarchical Approach (Divide and Conquer)
Car parts are not a flat list; they exist in a physical hierarchy. You can mirror this physical reality in your ML architecture using **Hierarchical Classification**.

* **Level 1 (Zone/System Model):** The multimodal inputs first go to a high-level model that predicts the general area or system (e.g., `Front Left`, `Powertrain`, `Undercarriage`, `Rear Bumper Assembly`).
* **Level 2 (Component Models):** If the Level 1 model flags the `Front Left` as damaged, the data is routed only to the "Front Left Sub-Model," which predicts specific parts (e.g., `Left Headlight Housing`, `Left Fender`, `Left Control Arm`).
* **Why this works:** Instead of one model choosing from 10,000 parts, you have a high-level model choosing from 15 zones, and specialized sub-models choosing from 100-200 parts each. It massively reduces the mathematical complexity and class imbalance.

### 2. The Retrieval/Recommendation Approach (Embedding Space)
Instead of treating this as a "classification" problem, treat it like a **Search Engine** or **Recommendation System** (like Netflix recommending movies).

* **How it works:** 
  1. You map all 10,000 possible parts into a database using text embeddings of their descriptions.
  2. You train your Multimodal Model (Images + Text + Telemetry) using **Contrastive Learning**. The goal is to make the embedding of the *crash data* mathematically similar to the embeddings of the *parts that need replacing*.
  3. When a new crash happens, the model outputs a single "Crash Vector." You run a **K-Nearest Neighbors (KNN)** search to retrieve all parts in your database that sit closest to this Crash Vector.
* **Why this works:** It natively supports multiple outputs (just retrieve the top $K$ nearest parts). More importantly, if the manufacturer releases a new car model with 500 *new* part numbers, you don't have to retrain the ML model—you just add the new parts to the vector database.

### 3. Knowledge Graphs & Graph Neural Networks (GNN)
In a collision, part damage is highly correlated based on physics. If the **Radiator** is smashed, the **AC Condenser** (which sits right in front of it) is almost certainly smashed too. A standard ML model doesn't inherently know this physics rule.

* **How it works:** You build a **Knowledge Graph** of the vehicle. Parts are "Nodes," and their physical connections are "Edges." 
* You use a **Graph Neural Network (GNN)** on top of your multimodal system. The base model makes initial predictions based on the images/text, and the GNN refines them by "passing messages" along the physical graph (e.g., "The model is 95% sure the outer door skin is destroyed, so propagate a 60% probability that the inner door actuator is also damaged, even if it can't be seen in the image").

### 4. Sequence Generation (Vision-Language Models / Generative AI)
Instead of predicting probabilities across a fixed list, use an architecture similar to ChatGPT or LLaMA, but trained on your multimodal data.

* **How it works:** You use a multimodal transformer model (like LLaVA or a custom encoder-decoder). 
* **Input:** The images, the narrative text, and the telemetry (converted to text, e.g., "Speed: 45mph, Impact: Front").
* **Output:** The model is trained to *generate a sequence of text* containing the exact part codes or descriptions. 
* **Example Output:** `["Part_1042_Front_Bumper", "Part_992_Radiator_Support", "Part_11_Airbag_Driver"]`.
* **Why this works:** Generative models are unconstrained by output layer size. They can output 1 part or 50 parts dynamically based on the prompt and data.

---

### Which one should you build?

**If you are building this for production today:**
Start with the **Hierarchical Approach**. It is the easiest to debug. If a mechanic complains that the model missed a broken control arm, you can easily check if the model failed at Level 1 (missed the suspension zone entirely) or Level 2 (knew the suspension was hit, but guessed the wrong part). 

**If you have a constantly changing parts catalog (OEMs, aftermarket, multiple car brands):**
Go with the **Retrieval/Recommendation Approach**. Building a Vector Database of parts allows infinite scalability without altering the neural network's fundamental architecture. 

**Pro-Tip for Handling "Multiple Parts" (Thresholding):**
Regardless of the method you choose, do not rely on a static $0.5$ confidence threshold. Some parts are cheap and critical for safety (e.g., brackets, sensors) — you might want the model to flag these for replacement even at $0.2$ confidence. Other parts are incredibly expensive (e.g., whole engine blocks) — you might require a $0.8$ confidence to automatically flag it, otherwise routing it to a human for manual review. Use **dynamic thresholding** per part.

Yes, there is a rich ecosystem of open-source libraries, frameworks, and datasets that you can use to build this system. You don't have to start from scratch. 

Depending on which part of the architecture you are building, here are the best open-source solutions and reference repositories available today:

### 1. Multimodal Fusion (Combining Image + Text + Telemetry)
Instead of manually coding the concatenation layers for your modalities, you can use these open-source AutoML frameworks specifically designed for multimodal data.

*   **AutoGluon-Multimodal (AutoMM) by AWS:** 
    *   **What it is:** A phenomenal open-source library designed specifically for fine-tuning foundation models on multimodal data. It natively understands how to take a dataset containing an image column, a text column, and tabular columns (telemetry) and fuse them into a single predictive model.
    *   **GitHub:** `github.com/autogluon/autogluon`
    *   **Why use it:** You can literally pass it a Pandas DataFrame where one column is the image path, one is the narrative, and the rest are telemetry stats, and it will handle the fusion architecture automatically under the hood.
*   **Ludwig by Uber:**
    *   **What it is:** A declarative machine learning framework. 
    *   **GitHub:** `github.com/ludwig-ai/ludwig`
    *   **Why use it:** You configure your model using a simple YAML file. You just declare your inputs (`image`, `text`, `numerical`) and your output (`category` or `set` for multi-label), and Ludwig compiles the PyTorch code for you.

### 2. Extreme Multi-Label Classification (XMC)
If your parts catalog contains thousands of potential parts, standard multi-label tools will fail. You need XMC libraries.

*   **PECOS (Predicting with Extreme Contextualized Subspaces) by Amazon:**
    *   **What it is:** A highly scalable library for XMC that handles millions of labels. It builds hierarchical clustering trees to narrow down predictions fast.
    *   **GitHub:** `github.com/amzn/pecos`
    *   **Why use it:** This is the industry standard for extremely large product/parts catalogs.
*   **napkinXC:**
    *   **What it is:** An extremely fast and lightweight C++/Python library for extreme multi-label classification using Probabilistic Label Trees (PLT).
    *   **GitHub:** `github.com/mwydmuch/napkinXC`
    *   **Why use it:** If you have severe class imbalance (which you will, with rare car parts) and limited compute resources, this model trains exceptionally fast.

### 3. Domain-Specific Repositories (Vehicle Damage)
To train your Vision backbone, you should utilize pre-existing open-source car damage datasets rather than labeling everything yourself.

*   **CarDD (Car Damage Detection Dataset):**
    *   **What it is:** Currently the best publicly available large-scale dataset specifically designed for vision-based car damage detection and segmentation.
    *   **GitHub / Web:** `cardd-ustc.github.io`
    *   **Why use it:** It contains thousands of high-resolution images with bounding boxes and masks for dents, scratches, cracks, and shatters. You can use their open-source models as a pre-trained feature extractor for your image pipeline before fusing it with text/telemetry.
*   **DashGuard (Collision Prediction):**
    *   **What it is:** An open-source deep learning framework for traffic accident prediction from dashcam videos using multimodal inputs.
    *   **GitHub:** `github.com/lmondonico/dashguard-accident-detection`
    *   **Why use it:** A great reference architecture for how to process visual data alongside sequential/temporal data (similar to your telemetry data).

### 4. Retrieval-Based System (Vector Databases)
If you decide to go the "Search Engine" route (where you map the crash data to the closest vehicle parts in an embedding space), refer to these architectures:

*   **AWS Samples: Automotive Damage Processing with Vector Databases:**
    *   **What it is:** An open-source reference architecture recently published by AWS. It uses multimodal embeddings (Amazon Titan) to convert car damage images and metadata into vector representations, storing them in a Vector Database for semantic search.
    *   **GitHub:** Search for the AWS sample repository tied to their "Simplify automotive damage processing with Amazon Bedrock" architecture. 
*   **xmc.dspy (In-Context Learning for XMC):**
    *   **What it is:** A very modern approach using LLMs and Retrieval for multi-label classification of massive catalogs (over 10,000 classes).
    *   **GitHub:** `github.com/KarelDO/xmc.dspy`
    *   **Why use it:** If you want to use Large Language Models (LLMs/VLM) instead of training a classifier from scratch, this repo shows how to use "Infer-Retrieve-Rank" to pick parts out of a massive list using only a handful of examples.

### Summary Recommendation for Your Stack:
If I were building this today, I would piece together the following open-source stack:
1.  **Vision Pre-training:** Fine-tune a YOLOv8 or ResNet model on the **CarDD dataset** to understand vehicle damage physics.
2.  **Multimodal Framework:** Use **AutoGluon-Multimodal** as your core PyTorch engine. Pass it your text narratives, telemetry features, and images.
3.  **Head / Output Layer:** If your parts list is < 500, let AutoGluon handle the multi-label output. If your parts list is > 1,000, extract the embeddings from AutoGluon and feed them into **PECOS** or **napkinXC** to handle the massive multi-label classification task.


# Recent Work



The landscape for multimodal vehicle damage assessment has evolved rapidly between late 2024 and early 2026, shifting away from traditional Convolutional Neural Networks (CNNs) toward **Multimodal Large Language Models (MLLMs)** and **Retrieval-Augmented Generation (RAG)** systems. 

Here is a breakdown of the latest work, papers, and industry architectures that directly apply to your goal of building a multimodal, multi-part replacement prediction system.

### 1. The Shift to Vision-Language Models (VLMs)
Instead of training separate image classifiers and text processors, the latest industry standard uses VLMs to process images, narratives, and telemetry simultaneously.
* **Project Damage Control (August 2025):** A major European consortium project (involving HPC and AI centers) successfully demonstrated using **Vision LLMs** for fleet management. Instead of just drawing bounding boxes around damage, their system ingests photos and driver narratives to generate a context-aware, structured JSON report detailing the damage severity, location, and required actions. This proved that VLMs can natively bridge visual damage with textual mechanic logic [1].
* **Zero-Shot Accident Analysis with MLLMs (September 2025):** Recent research tested frontier models like **Gemini 2.0** and **Pixtral Large** for traffic accident detection and assessment. Researchers found that integrating MLLMs with telemetry (V2X communications) allows the system to accurately describe the physics of a crash and the resulting damage with minimal fine-tuning, replacing heavily engineered pipeline architectures [2, 3].

### 2. State-of-the-Art in Extreme Multi-Label Classification (XMC)
Since your parts catalog is massive, the latest research in XMC is highly relevant. Relying on standard classification heads is now considered outdated.
* **ViXML (Vision-Enhanced eXtreme Multi-Label Learning) (November 2025):** This is a breakthrough paper for your exact problem. Researchers proposed the ViXML framework, which scales XMC to massive catalogs by fusing visual and textual data. It integrates a frozen foundation vision model (to extract a single embedding per image) with text token embeddings [4]. It proved that adding visual metadata to Large Language Models drastically improves precision when choosing among millions of potential labels (or parts) [5, 6].
* **LLMs vs. AttentionXML (January 2025):** A comprehensive evaluation compared traditional XMC algorithms against fine-tuned LLMs (like LLaMA-3 and Mistral). The study concluded that applying **Low-Rank Adaptation (LoRA)** to open-weight LLMs allows them to match or beat dedicated mathematical tree-based models for massive catalog classification [7]. *Takeaway: You can fine-tune an open-source LLM to predict your parts list rather than building a custom XMC neural network from scratch.*

### 3. AWS "Vector Database" Reference Architecture (Nov 2024)
If you want to build this system for production today, Amazon Web Services recently published a reference architecture specifically for **Automotive Damage Processing**. 
* **How it works:** AWS uses **Amazon Titan Multimodal Embeddings** to ingest the damage image alongside text metadata (make, model, narrative, telemetry). It converts this entire multimodal package into a single mathematical vector [8]. 
* **The Prediction:** It stores the historical database of replaced parts in **OpenSearch** (a vector database). When a new crash occurs, it performs a semantic similarity search to retrieve the exact repair estimates and part numbers from historical crashes that mathematically match the current crash's multimodal vector [8]. This avoids the "10,000 class output layer" problem entirely [8].

### 4. Telemetry Fusion Innovations
Fusing structured telemetry data (speed, G-force) with unstructured images/text is challenging. Recent papers have introduced new fusion frameworks:
* **The REACT Framework (August 2025):** This research introduced an edge-based multimodal sensor fusion system using a lightweight VLM (only 512M parameters). It aligns telemetry data (spatial-temporal inputs) with visual data using "spatial grounding enhancement." This is highly relevant if your telemetry data involves time-series sensor readings leading up to the crash [9].
* **Multi-Modal Autoencoder Fusion (October 2025):** A new study successfully used early-fusion and decision-level fusion to combine IMU (accelerometer/G-force) data, audio, and visual data. They utilized a multi-modal ensemble model to achieve 92% ROC-AUC in real-time minor damage detection, proving that adding physical telemetry to vision models drastically reduces false positives [10].

### 5. Advances in the Vision Backbones
If you still want to build a hierarchical system (detecting the damaged area first, then predicting the part), the vision backbones have become highly specialized for car damage:
* **HL-YOLO (November 2025):** A newly proposed architecture (Heterogeneous Convolutions and Large-Kernel Attention) specifically optimized for vehicle damage. It vastly improves the model's ability to localize complex damage (like warped frames or structural crumpling) compared to standard YOLOv8 [11].
* **Component-Damage Association via Mask R-CNN (October 2025):** Recent studies have perfected training instance segmentation models on large-scale datasets to automatically link a specific visual defect (e.g., a dent) to the exact exterior component (e.g., left fender), creating a highly structured visual input that can be fed into a rule-based engine or LLM for final part replacement recommendations [12].

**Summary of How to Apply the Latest Work:**
Instead of building a traditional Multi-Layer Perceptron fusion network, the 2025/2026 approach is to use a **Multimodal Embedding Model** (like Amazon Titan or an open-source equivalent like Qwen-VL) to project your Images, Telemetry, and Narrative into a joint vector space. You then use a **Vector Database (RAG)** or an **XMC-adapted LLM (like ViXML)** to retrieve the exact parts that need replacing from your massive catalog[4, 8].