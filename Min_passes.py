'''10. Minimum Passes to Sort Using Selection Strategy

Each pass places the correct minimum element at position i.

Return the minimum number of passes needed to completely sort the array.'''


a = [2,1,3,4]
swaps = 0

for i in range(len(a)):
    min_index = i
    for j in range(i+1,len(a)):
        if  a[j] < a[min_index]:
            min_index = j

    if min_index != i :
        a[i],a[min_index] = a[min_index],a[i]
        swaps += 1

print(a)
print(swaps)

