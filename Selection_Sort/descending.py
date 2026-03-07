#3. Sort in Descending Order
#Use selection sort to sort this list from largest to smallest.


a = [7, 2, 9, 1, 5]

for i in range(len(a)-1):
    min_i = i
    for j in range(i+1,len(a)):
        if a[j] > a[min_i]:
            min_i = j
    a[i],a[min_i] = a[min_i],a[i]

print(a)

