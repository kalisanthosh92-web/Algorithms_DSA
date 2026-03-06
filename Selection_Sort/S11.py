#Use selection sort to find the largest element.

arr = [2, 8, 1, 10, 4]

max_val = arr[0]

for i in arr:
    if i > max_val:
        max_val = i

print(max_val)