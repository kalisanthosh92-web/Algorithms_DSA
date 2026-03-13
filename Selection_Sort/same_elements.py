a = [4,1,3,1,2]
comp = 0
k = 1
for i in range(len(a)-1):
    if k <= 0:
        break
    min_i = i
    for j in range(i+1,len(a)):
        comp += 1                   #note this
        if a[j] < a[min_i]:
            min_i = j
    if min_i != i:
        a[i],a[min_i] = a[min_i],a[i]
        k -= 1
        
print(a)
print(comp)

