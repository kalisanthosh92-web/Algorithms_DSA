#Write a program that prints the list after every pass of selection sort

a = [5, 3, 8, 4]

for i in range(len(a) - 1):
    min_i = i 
    for j in range(i+1,len(a)):
        if a[j] < a[min_i]:
            min_i = j
    a[i],a[min_i] = a[min_i],a[i]
    print(f'pass {i +1}:{a}')

print(a)