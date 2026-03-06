#Sort the list using selection sort.

a = [12, 4, 8, 1, 6]


for i in range(len(a)):
    min_i = i
    for j in range(i+1,len(a)):
        if a[j] < a[min_i]:
            min_i = j
    a[i],a[min_i] = a[min_i],a[i]

print(a)

