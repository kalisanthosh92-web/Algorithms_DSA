#Write selection sort that places the largest element at the end each pass.

a = [4,2,7,1]

for i in range(len(a)-1,0,-1):
    max_i = 0
    for j in range(1,i+1):
        if a[j] > a[max_i]:
            max_i = j
    a[i],a[max_i] = a[max_i],a[i]

print(a)
