#Write selection sort and count the number of swaps performed.
a =  [5, 2, 4]
r = 0
for i in range(len(a)):
    min_i = i
    for j in range(i+1,len(a)):
        if a[j] < a[min_i]:
            min_i = j

    if i != min_i:
        a[i],a[min_i] = a[min_i], a[i]
        r += 1
        
print(a)
print(r)

