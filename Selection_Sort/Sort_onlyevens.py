'''5. Sort Only Even Numbers
Problem
Sort only the even numbers in the list using selection sort while keeping odd numbers in their original positions.'''




a = [5,8,3,2,1,4]
k = []

for i in a:
    if i%2 == 0:
        k.append(i)

for i in range(len(k)):
    min_i = i 
    for j in range(i+1,len(k)):
        if k[j] < k[min_i]:
            min_i = j 
    k[i],k[min_i] = k[min_i],k[i]

x = 0 
for i in range(len(a)):
    if a[i]%2 == 0:
        a[i] = k[x]
        x += 1
    
print(a)



