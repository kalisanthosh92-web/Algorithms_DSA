'''1. Sort the Array

Problem

Given an integer list nums, sort the list using selection sort.

Return the sorted list.

Example
'''



a = [4,3,2,1]
swaps = 0
for i in range(len(a) - 1):
    min_i = i
    for j in range(i+1,len(a)):
        if a[j] < a[min_i]:
            min_i = j
    a[i],a[min_i] = a[min_i],a[i]

    if min_i != i:
        swaps += 1
print(a)
print(swaps)