# Youtube Recommendation Engine

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
 Build a video recommendation system for Youtube users. We want to maximize users engagement and recommend new types of content to users.

### 1. Gathering Requirements
1. Size and Scale of the high level system

	1. Total number of users - 1.3 billion
	2. Total videos > 1billion
	3. Videos viewed per month 150 billion
	4. 10% of videos watched are from recommendations, a	 total of 15 billion videos.
	5. On a homepage, user sees 100 video recommendations.

2. User data

	1. User profile data - age, gender ,location
	2. User Feedback data - video views, time spent on each videos,likes, comments, followings 
	3. User interests - genres, topics

3. Video Data

	1. Channel Information
	2. Annotated metadata - topic, linked data , title , size , description
	3. Number of views , likes, comments

4. Recommendations

	1. On average, user watches 2 out of 100 videos
	2. If a user doesnt watch some video within a given time frame ,i.e 10 minutes then it it is missed recommendations.
	3. Bandwidth
		1. Assume a need to generate a recommendation request every second for 10 million users.
		2. Each user will generate rank for 1k-10k videos.

5. Data Size
	1. For 1 monthm we collected 15 billion positive labels and 750 billion negative labels.
	2. With every data point , we collect hundred of features,For simplicity each row takes 500 bytes to store.In 1 month , we need 800 billion rows.
	3. Total size - 500* 800* 10^9 = 4 * 10^14 bytes = 0.4 petabytes.
	4. To save cost, we can keep the last size months or one year of data in the data lake, and archive old data in cold storage.

6. Scale
	1. Support 1.3 billion users
	2. Support > 1 billion videos
	3. Hae distributed ML servers for training and inference.
	4. Have load balancers.

7. Training
	1. User behavior is generally unpredictable, and videos can become viral during the day.
	2. Ideally, we want to train many times during the day to capture temporal changes.

8. Inference
	1. For every user to visit the homepage, 		the system will have to recommned 100 videos for them. The latency needs to be under 200 ms, ideally less than 100 ms.
	2. For online recommnedations, its important to find the balance between exploration and exploitation.
		1. We want to balance between the relevancy and fresh new content.

9. Defining End Goal
	1. Metrics - Reasonable Precision, high recall
	2. Training - 	High throughput with the ability to retrain many times 	per day.
	3. Inference - Latency from 100 ms to 200 ms. Flexible to control exploration versus exploitation


### 2. Define Metrics

Online Metric
1. Click through rate
2. Successful sessions (watch times)
3. Conversion rates
4. Additional inputs - lkes,subscribe , follow ,comments.


Offline Metrics
1. Precision
2. Recall
3. F1 Score
4. PR curve (class imbalance)

### 3. High Level Architecture

ML component

Non ML component


## 4. Building System Componenets

1. Data
	1. Training Data Generation
	2. Hand Labelled Data
	3. Implicit data from logs
	4. Advanced labeling
		1. Semi Supervised Approach
	5. Feature Engineering
		1. One hot encoding,Feature Hashing,NN Embedding
		2. Standardisation /Normalization
		3. Missing Value Treatment	
2. Data Ops
	1. Data Storage
		1. Object Storage
		2. Database for metadata
		3. FeatureStore
		4. Data versioning
	2. Data Injestion and transform
		1. Offline Data Can query database
		2. Online Data- High throuhput low latency,online or streaming service using Apache Kafka,RabbitMQ
		3. Feature Transformation - Apache Spark,Tensorflow Transform
		4. Orchestration
			1. Airflow
			2. Kubernetes
3. Computing Resource - Edge ,Cloud
4. Learning Modes - Offline learning and online learning
5. Inference Modes - Batch and online
6. ML Model and Architecture
	1. Candidate Generation
	2. Ranking
7. ML Ops
	1. Repeatability of Experiments: ML Flow, Kubeflow
	2. Parallelize HP tuning on cloud.
	3. Model versioning 
7. Serving	
	1. Online A/B Testing
	2. Where to run inference
		1. User's phone or computer - low latency but high memory and battery usage.
		2. On company service - increased latency and privacy concerns but no device-level challenges.

	3. Monitoring Performance
		1. Log Error Rates
		2. Time to return queries
		3. Metric Score

	4. Biases and Misuse of the model
	5. How often to retrain the model
	6. Store logs in a database like Elastic Search,Logstash
	7. 	Logging Analytics tool: Kibana ,Splunk
	8. CI/CD: Circle CI, Travis CI
	9. Deploying on Embedded and Mobile Device
		1. Quantisation
		2. Reduced model size
		3. Knowledge Distillation

		
#### ML Algorithm

1. Candidate Generation

	1. Content Based Filtering
		1. Item-Item Similarity
		2. Advantages-
			1. No info required for other user.Easier to scale to a large number of users.
			2. Can capture specific interest of user and recommend niche items that very few other users are interested in.
		3. Disadvantage
			1. Feature Representation of items are hand engineered ,hence requires domain knowledge.
			2. Limited ability to expand 	on user's exisiting interests.
	2. Collaborative Filtering[CF]
		1. Advantages
			1. No domain knowledge necessary- as embeddings are already learned.
			2. Model can help users discover new interests.
			3. System only needs a feedback matrix to train a matrix factorization model and not contextual features.
		2. Disadvantages
			1. Cannot handle fresh items - cold start problem.
			2. Heurisitic to generate embeddings of fresh items.
			3. Hard to include side features for query or item.
				1. Generalization of WALS by augmenting the input matrix with features.
		1. User-User CF
			1. Recommend items based on similar users.
			2. Too many users on the platform,doesnot scale well.
		2. Item-Item CF
			1. Recommend items based on similar videos watched by users.
			2. Too many new videos uploaded on platform.Doesnot scale well.
		3. User-Item - Too much space required. O(mn)

		

2. Matrix Factorization used in Collaborative Filtering
	1. Project videos and users in the same space for direct comparision.
	2. Computationally efficient
	3. No interpretability
	4. Optimisation Algorithm
		1. SGD
		2. Weighted Alternating Least Square.
	4. USV[T] - U- User Matrix, S- Latent Space[Diagonal Matrix] , V[T] - Item Matrix
3. Deep Learning Based
		

		
