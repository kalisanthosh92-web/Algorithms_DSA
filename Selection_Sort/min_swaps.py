'''8. Minimum Swap Selection Sort

Problem

Use selection sort but avoid unnecessary swaps.

Return the number of swaps used.'''




a = [1,2,3,4]
swaps = 0
for i in range(len(a)):
    min_i = i
    for j in range(i+1,len(a)):
        if a[j] < a[min_i]:
            min_i = j 


    if min_i != i:
        a[i],a[min_i] = a[min_i],a[i]
        swaps += 1

print(a)
print(swaps)


