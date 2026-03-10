'''8. Index Mapping After Selection Sort

Return an array showing where each original index moves after selection sort.'''


n = [50,20,40]
original = n.copy()
x = []

for i in range(len(n)):
    min_i = i
    for j in range(i+1,len(n)):
        min_i = j 

    n[i],n[min_i] = n[min_i],n[i]

for i in range(len(n)):
    original_idx = original.index(n[i])
    x.insert(i,original_idx)


print(x)