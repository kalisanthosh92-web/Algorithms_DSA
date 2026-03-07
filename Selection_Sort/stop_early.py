#9. Stop Early if Sorted
#Modify selection sort to stop early if the list becomes sorted.


arr = [1, 2, 3, 4, 5]

for i in range(len(arr)):
    min_i = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_i]:
            min_i = j

    if i == min_i:
        continue

    arr[i], arr[min_i] = arr[min_i], arr[i]

print(arr)