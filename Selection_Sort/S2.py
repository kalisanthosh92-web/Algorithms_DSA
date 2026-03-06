#Modify selection sort to sort numbers in descending order.


a = [4, 1, 7, 3]
for i in range(len(a)):
    min_i = i
    for j in range(i+1,len(a)):
        if a[j] < a[min_i] :
            min_i = j
    a[i],a[min_i] = a[min_i], a[i]

print(a)

