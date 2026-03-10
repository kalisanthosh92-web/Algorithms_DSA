'''2. K Pass Selection Sort

Perform only the first k passes of selection sort on the array.

Return the array after k passes.'''



n = [7,4,5,12,15,11,10,2,9]
k = 2
swaps = 0

for i in range(len(n)):
    min_i = i
    for j in range(i+1,len(n)):
        if n[j] < n[min_i]:
            min_i = j 
        
    if min_i != i:
        n[i],n[min_i] = n[min_i],n[i]
        swaps += 1
    if swaps == k :
        print(n)
        break 


print(swaps)
