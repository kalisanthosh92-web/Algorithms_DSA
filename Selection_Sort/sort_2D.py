#10. Sort a 2D List by First Element
#Use selection sort to sort this list by the first number in each sublist.


a = [[3, 90], [1, 80], [2, 70]]


for i in range(len(a) - 1):
    min_i = i
    for j in range(i+1,len(a)):
        if a[j][0] < a[min_i][0]:
            min_i = j
    a[i],a[min_i] = a[min_i],a[i]

print(a)

