#5. Selection Sort Without Swap
#Instead of swapping immediately, store the minimum and place it after the loop.


a = [11, 25, 12, 22, 64]

for i in range(len(a) - 1):
    min_i = i
    for j in range(i+1,len(a)):
        if a[j]< a[min_i]:
            min_i  = j

    temp = a[min_i]
    del a[min_i]
    a.insert(i,temp)
    



print(a)