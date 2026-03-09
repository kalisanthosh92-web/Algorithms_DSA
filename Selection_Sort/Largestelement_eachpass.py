'''6. Largest Element Each Pass
Problem
Modify selection sort to pick the largest element each pass and place it at the end.
Return the sorted list.'''


a = [3,1,4,2]


for i in range(len(a)-1,-1,-1):
    min_i = i
    for j in range(i-1,-1,-1):
        if a[j] > a[min_i]:
            min_i = j 

    large = a[min_i]

    if min_i != i:
        del a[min_i]
        a.insert(i,large)
        


print(a)

