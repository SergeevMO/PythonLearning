def grow_list(a, lst=[]):
    lst.append(a)
    print('lst ', id(lst))
    return lst

lst1 = grow_list(1)
print('lst1 ', id(lst1))
lst3 = [3]
print('lst3 ', id(lst3))
lst1 = grow_list(2, lst3)
print('lst1 ', id(lst1))
lst2 = grow_list('a')
print(lst1)
print(lst2)
print(id(lst1), '\n', id(lst2), sep='')