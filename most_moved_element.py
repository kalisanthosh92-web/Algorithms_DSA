'''3. Find the Element Moved Most

While performing selection sort, track how far each element moves from its original index.

Return the maximum distance moved by any element.'''



n = [4,3,2,1]
swaps = 0
original = n.copy()
for i in range(len(n)):
    min_i = i
    for j in range(i+1,len(n)):
        if n[j] < n[min_i]:
            min_i = j 
        n[i],n[min_i] = n[min_i],n[i]
        
max_move = 0
for i in range(len(n)):
    old_index = original.index(n[i])
    max_move = max(max_move,abs(i-old_index))

print(max_move)