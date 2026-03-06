#Write selection sort that sorts only even numbers and leaves odd numbers in place.

a = [7, 4, 3, 8, 5, 2]

evens = []
for x in a:
    if x%2 == 0:
        evens.append(x)


for i in range(len(evens)):
    min_i = i 
    for j in range(i+1,len(evens)):
        if evens[j] < evens[min_i]:
            min_i = j
    evens[i],evens[min_i] = evens[min_i],evens[i]

k = 0 
for i in range(len(a)):
    if a[i]%2 == 0:
        a[i] = evens[k]
        k += 1
print(a)

