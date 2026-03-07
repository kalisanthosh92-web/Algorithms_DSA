#6. Sort Strings
#Use selection sort to sort this list of strings alphabetically.


words = ["banana", "apple", "cherry", "mango"]

for i in range(len(words) - 1):
    min_i = i 
    for j in range(i+1,len(words)):
        if words[j] < words[min_i]:
            min_i = j

    words[i],words[min_i] = words[min_i],words[i]

print(words)

