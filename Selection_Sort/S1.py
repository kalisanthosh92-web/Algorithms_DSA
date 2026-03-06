#Write a program to sort a list in ascending order.

#st = list(input('Enter a list:'))

def smallest(lst):
    smallest = lst[0]
    s_index = 0
    for i in range(1,len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
            s_index = i
    return s_index

def Selectionsort(lst):
    newarr = []
    for i in range(len(lst)):
        smallest = smallest(lst)
        newarr = newarr.append(lst.pop(smallest))
    return newarr

print(Selectionsort([29,10,14,377,13]))



