#Write a program to sort a list in ascending order.

lst = eval(input('Enter a list:'))

def smallestnum(lst):
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
        smallest = smallestnum(lst)
        newarr.append(lst.pop(smallest))
    return newarr

print(Selectionsort(lst))



