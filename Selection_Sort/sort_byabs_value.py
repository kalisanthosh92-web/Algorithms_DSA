'''7. Sort by Absolute Value

Problem

Sort numbers using selection sort based on absolute value.'''



a = [-4,2,-1,3]

for i in range(len(a)):
    min_i = i
    for j in range(i+1,len(a)):
        if abs(a[j]) < abs(a[min_i]):
            min_i = j 
    a[i],a[min_i] = a[min_i],a[i]

print(a)

