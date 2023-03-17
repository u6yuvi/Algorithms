# Object Detection in Documents

## Framework

1. Gather all the requirements about the system.
2. Define Metrics and Evaluation Criteria
	1. Offline Metrics
	2. Online Metrics
3. High Level Architecture Design
4. Building system components for Offline model building and evaluation.
	1. Data Generation
	2. Feature Engineering
	3. Model Training and Evaluation

5. Deep Dive in 1-2 critical questions/components
	1. Pick a critical component that you are confident of.
	2. Go deeper into the details of data ,modeling,evaluation and shortcomings.
	3. Propose potential ways to improve.
	4. Other considerations to highlight
		1. Class Imbalance
		2. Noisy Labels
		3. Calibration

6. Scaling , Monitoring ,Logging , Alerts
	1. Scaling
	2. Model Performance and data monitoring
	3. Model Retraining
	4. Model Updates
	5. Identify potential system failures
		1. Miscalibrated predictions,online metrics degradation etc.


## Problem Statement

Design a System that can recognize different regions in the Document. Different regions could be :
1. Text
2. Title
3. Table
4. Logo
5. Header
6. Footer
7. Image Patch
8. Seal

## Gathering Requirements

1. Size and Scale of the high level system
	
	1. Upper threshold of per page extraction time ~ 200 ms considering 1 document of avg 5 pages with 20% time going into Object Detection and Extraction Module
	2. Time to process 1 image = 100~200ms on GPU
	3. Time to process 1 image on CPU -1-2 sec
	4. No of categories to predict - 8[text,title]
	5. Any futher addition of labels in future - No

	5. Available data
		1. 1500 images with an average of 4 labels per image.
		2. Around 6000/8 images / category ~ 750
		3. Image size - 800,750 pixels i.e 500KB 
	6. Retraining
		1. Every quarter new doc_type is added which may or maynot bring new variety of data for each category.
		2. Considering retraining every quarter


2. Metric 
	1. Offline Metric
		1. Precision 
		2. Recall 
		3. F1 Score
		4. Average Precision

	2. Online Metric
		1. Final Document Extraction Accuracy 

3. High Level Architecture Design



4. System Componenets

	1. Data
		1. Storage -File Object Storage,
		2. Tracking - dvc
		3. Labeling 
			1. Weak supervision - Using any pretrained model to annotate.
			2. Using Image Processing algorithms to detect regions.
			3. Hand labeling
				1. Tools
					1. Labelme
					2. Label Studio
				
		4. Train-Test split 
			1. Stratified Sampling 

	2. Image PreProcessing 
		1. Different IP filters 
	
	3. Image Clustering
		1. Use Representation Learning to convert image into Embeddings and use clustering to cluster documents
			1. Clustering Distance Metric 
				1. Euclidean Distance
		2. Select topk images from each clusters and start tagging.Ensures tagging of different variety of document images.
		3. Also can be used to identify anomoly in case the number of images per cluster is low.
	
	4. Model Selection
		1. Single Stage Detection Algorithm eg. Yolo , Single Shot Detections[SSD]
			1. Provides faster inference
			2. Might be lower on performance from Two Stage Detection Algorithms
		2. Two Stage Detection Algorithm 
			1. Region Proposal based Networks

	5. Model Training
		1. Use Transfer Learning for finetuning the model on our dataset.
		2. Model training from scratch,if our data is unique in terms of image characterisitcs. 
		
	5. Model Optimisation
		1. Tracing using TorchScript
		2. Quantisation 

	6. Model Inference
		1. Can be optimised using Adaptive Batching .For eg Torch Serve , ML Serve
		2. Image Preprocessing and Resizing before sending the reques to reduce the response time of processing the request.

		3. Use serialisation of image while sending request.
		3. Use Rest or GRPc API protocol to send and receive request.

	7. Model Experimentation
		1. A/B Testing to evaluate model performance on Extraction Accuracy.

	8. Monitoring and Logging
		1. Log Model Confidence Score per category and observe the std over time.
		2. Log model latency (ms) to observe request processing time over time.

	


