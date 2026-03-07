#4. Find Number of Comparisons
#Modify selection sort to count the number of comparisons.


a = [4, 2, 6, 1]
comp = 0
for i in range(len(a)-1):
    min_i = i
    for j in range(i+1,len(a)):
        comp += 1                   #note this
        if a[j] < a[min_i]:
            min_i = j
            
    a[i],a[min_i] = a[min_i],a[i]
    

print(a)
print(comp)

