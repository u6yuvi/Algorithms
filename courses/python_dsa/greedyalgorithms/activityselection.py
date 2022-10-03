'''
Given N number of activities with their start and end times. 
We need to select the maximum number of activities that can be performed 
by a single person, assuming that a person can only work on a single 
activity at a time.
'''

#PseudoCode

'''
1. Sort the activity by end time
2. for each acitity:
    Select the next activities where curr activity end time < next activity start time 
'''

def Activity(activities):
    activities.sort(key = lambda x : x[2])
    i = 0
    activity = []
    activity.append(activities[i][0])
    for j in range(len(activities)):
        if activities[j][1] >= activities[i][2]:
            activity.append(activities[j][0])
            i = j
        
    return activity



activities = [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9]
                ]

assert Activity(activities) == ['A3', 'A2', 'A5', 'A6']

