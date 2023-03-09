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

### Gathering Requirements
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


### Define Metrics

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

### High Level Architecture

ML component

Non ML component

		
