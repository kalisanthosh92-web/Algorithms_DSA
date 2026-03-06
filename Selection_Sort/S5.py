#Sort a list using selection sort but return a new list without modifying the original.

a = [8, 3, 5]
b= a.copy()

for i in range(len(b)):
    min_i = i
    for j in range(i+1,len(b)):
        if b[j] < b[min_i]:
            min_i = j
    b[i],b[min_i] = b[min_i],b[i]

print(a)
print(b)

