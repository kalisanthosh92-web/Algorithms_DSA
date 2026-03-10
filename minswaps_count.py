'''1. Count Minimum Selection Swaps

Given an integer array nums, sort the array using selection sort.

Return the number of swaps performed.'''


n = [5,2,4,6,1]
swaps = 0
for i in range(len(n)):
    min_i = i
    for j in range(i+1,len(n)):
        if n[j] < n[min_i]:
            min_i = j 
        
    if min_i != i:
        n[i],n[min_i] = n[min_i],n[i]
        swaps += 1

print(n)
print(swaps)