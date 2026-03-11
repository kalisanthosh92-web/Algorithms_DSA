'''9. Selection Sort Stability Check

Selection sort is usually not stable.

Given an array of tuples (value, id), perform selection sort by value.

Return the sorted list and determine whether relative order of equal values changed.'''



a = [(4,'a'),(3,'b'),(4,'c')]
original = a.copy()

for i in range(len(a)):
    min_i = i 
    for j in range(i+1,len(a)):
        if a[j][0] <= a[min_i][0]:
            min_i = j
    a[i],a[min_i] = a[min_i],a[i]

stable = True

for i in range(len(a)-1):
    if a[i][0] == a[i+1][0]:
        if original.index(a[i]) > original.index(a[i+1]):
            stable = False 



print(a)
print("Stable:", stable)