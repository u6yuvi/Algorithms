a = [2,4,32,5,1]
print(len(a))

for i in range(len(a)-1):
    #print(a[i])
    min_v = a[i]
    min_i = i
    for j in range(i+1,len(a)-1):
        if a[j] <= min_v:
            min_v = a[j]
            min_i = j
    a[i] , a[min_i] = a[min_i], a[i]

print(list(range(0,len(a))))

a = [2,4,32,5,1]
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] >= a[j+1]:
            a[j] , a[j+1] = a[j+1] , a[j]
print(a)