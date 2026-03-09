'''4. Minimum Element Each Pass

Problem

During selection sort, store the minimum value selected in each pass.

Return the list of these minimums.'''




a= [6,4,2,7]
mins = []
for i in range(len(a) - 1):
    min_i = i
    for j in range(i+1,len(a)):
        if a[j] < a[min_i]:
            min_i = j
    
        if min_i != i:
            mins.insert(i,a[min_i])
    
    a[i],a[min_i] = a[min_i],a[i]

    

print(a)
print(mins)
