#Use selection sort to find the smallest number without sorting the entire list.

a = [9, 7, 3, 5,4,8]
min_val = a[0]
for i in a:
    if i < min_val:
        min_val = i

print(min_val)

