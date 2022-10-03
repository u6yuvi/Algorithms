# Called lazy learning method as no work is done until a prediction is required.

#Learning Path
'''
1. Theory
https://www.youtube.com/watch?v=Jtmh21_FAoU&list=PLBv09BD7ez_48heon5Az-TsyoXVYOJtDZ&index=2

2. Learn the Basic Implementation
https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

This k-Nearest Neighbors tutorial is broken down into 3 parts:

Step 1: Calculate Euclidean Distance.
Step 2: Get Nearest Neighbors.
Step 3: Make Predictions.

'''

from math import sqrt

dataset = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,1],
	[1.38807019,1.850220317,1],
	[3.06407232,3.005305973,1],
	[7.627531214,2.759262235,0],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]


def eucliean_distance(row1,row2):
    distance = 0
    for i in range(len(row1)-1): #last row to be target variable
        distance += (row1[i]-row2[i])**2
        return sqrt(distance)


def get_neighbours(train,test_row,k):
    distances = []
    for train_row in train:
        distance = eucliean_distance(train_row,test_row)
        distances.append((train_row,distance))
        distances.sort(key = lambda x : x[1])
    
    neigbours = []
    for i in range(k):
        neigbours.append(distances[i][0]) # return records

    return neigbours


def predict_classification(train,test_row,k):
    neigbours = get_neighbours(train,test_row,k)
    labels = [i[-1] for i in neigbours]
    pred = max(set(labels),key = labels.count)
    return pred


def dataset_minmax(dataset):
    minmax = []
    for col_idx in range(len(dataset[0])-1):
        colvalues = [ row[col_idx] for row in dataset]
        value_min = min(colvalues)
        value_max = max(colvalues)
        minmax.append((value_min,value_max))
    return minmax

def min_max_normalization(dataset,minmax):
    for row in dataset:
        for i in range(len(row)-1):
            row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])




MINMAX = dataset_minmax(dataset)
print('Before normalisation\n',dataset)
print(min_max_normalization(dataset,MINMAX))
print('After normalisation\n',dataset)

print(predict_classification(dataset,dataset[0],6))