'''3. Kth Position After Selection Sort

Problem

After performing selection sort on nums, return the element at index k.
'''


a = [8,3,5,2,9]



for i in range(len(a) - 1):
    min_i = i
    for j in range(i+1,len(a)):
        if a[j] < a[min_i]:
            min_i = j
    a[i],a[min_i] = a[min_i],a[i]

k = int(input('Enter the \'k\' position:'))
print(a[k])
    