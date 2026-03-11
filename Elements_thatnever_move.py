'''2. Count Elements That Never Move

Count how many elements stay in the same position after selection sort.'''


a = [3,1,2,4]
n = a.copy()
same_position = 0
for i in range(len(a)):
    min_i = i
    for j in range(i+1,len(a)):
        if a[j]<a[min_i]:
            min_i = j

    a[i],a[min_i] = a[min_i],a[i]

for i in range(len(a) ):
    original_idx = n.index(a[i])
    if a[i] == n[i]:
        same_position += 1

print(a)
print(same_position)
print(n)