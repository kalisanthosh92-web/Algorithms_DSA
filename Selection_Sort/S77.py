#Sort a 2D list based on the first element using selection sort.

a = [[3,5],[1,2],[4,1]]

for i in range(len(a)):
    min_i = i
    for j in range(i+1,len(a)):
        if a[j] < a[min_i]:
            min_i = j 
    a[i],a[min_i] = a[min_i],a[i]

print(a)

