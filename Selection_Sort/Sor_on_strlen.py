#7. Sort Based on String Length
#Sort strings using selection sort based on length of words.

words = ["python", "ai", "data", "code"]


for i in range(len(words)):
    min_i = i 
    for j in range(i+1,len(words)):
        if len(words[j]) < len(words[min_i]):
            min_i = j

    words[i],words[min_i] = words[min_i],words[i]

print(words)

