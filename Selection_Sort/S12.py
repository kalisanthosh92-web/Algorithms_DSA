#Write selection sort that sorts only even numbers and leaves odd numbers in place.

a = [7, 4, 3, 8, 5, 2]
min_j = 0
for i in range(len(a)):
    
    for j in range(i+1,len(a)):
        if a[j]//2 == 0 and a[i]//2 == 0:
            if a[j] > a[i]:
                a[i],a[j] = a[j],a[i]
    
                    
        
print(a)   
