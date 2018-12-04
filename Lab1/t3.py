
list1 = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]

list2 = []
def my_fun(list1):
    for x in list1:
        if type(x) == list:
            my_fun(x)
        else:
            list2.append(x)


my_fun(list1)
print(list1)
print(list2)
