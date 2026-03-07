#Modify selection sort to count how many swaps are performed.

a = [5, 3, 8, 4, 2]
swaps = 0
for i in range(len(a)-1):
    min_i = i
    for j in range(i+1,len(a)):
        if a[j] < a[min_i]:
            min_i = j


    if i != min_i:
        a[i], a[min_i] = a[min_i], a[i]
        swaps += 1



print(a)
print(swaps)
