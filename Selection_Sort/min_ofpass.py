#8. Find Minimum Each Pass
#Modify selection sort to print the minimum value found in each pass.


a = [9, 4, 6, 2]

for i in range(len(a)-1):
    min_i = i
    for j in range(i+1,len(a)):
        if a[j]< a[min_i]:
            min_i = j 
    print(f'pass {i+1} min {a[min_i]}')    
    a[i],a[min_i] = a[min_i],a[i]

print(a)