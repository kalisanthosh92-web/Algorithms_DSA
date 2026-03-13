a = [5,1,4]
passes = 0
print(a)
for i in range(len(a) ):
    
    min_i = i
    for j in range(i+1,len(a)):
        passes +=1
        if a[j] < a[min_i]:
            
            print(f'{a[min_i]} vs {a[j]}')   
            min_i = j
        else:
            print(f'{a[min_i]} vs {a[j]}')   
           
    

    if min_i != i:
        a[i],a[min_i] = a[min_i],a[i]
    
print(passes)