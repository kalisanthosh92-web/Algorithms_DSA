'''
6. Detect Selection Sort Pass

You are given:

the original array

a partially sorted array

Determine whether the partially sorted array could appear during selection sort.'''




original = [5,3,8,4,2]
partial  = [2,3,8,4,5]

found = False

for i in range(len(original)):
    min_i = i 
    for j in range(i+1,len(original)):
        if original[j]<original[min_i]:
            min_i = j

    original[i],original[min_i] = original[min_i],original[i]

    if original == partial:
        found = True 
        break

print(found)
