from math import *

def First_Task(cort):
    
    isint = True
    
    for element in cort:
        try:
            int(element)
        except ValueError:
            isint = False
    
    if isint:
        r = tuple(int(el) for el in cort)
        sorted_r = tuple(sorted(r))
        print(sorted_r)
    else:
        print(tuple(cort))

def Second_Task(cort, el):
    f_ind = -1
    for i in range(len(cort)):
        if cort[i] == el:
            f_ind = i
            break
    if f_ind != -1:
        s_ind = -1
        for i in range(i+1, len(cort)):
            if cort[i] == el:
                s_ind = i
        
        if s_ind != -1:
            print(cort[f_ind:s_ind])

        else:
            print(cort[f_ind:])
    else:
        print(tuple())

def Third_Task(arr):
    print(f"Множество: {set(arr)}, мощность: {len(set(arr))}")

def Fourth_Task(arr):
    from collections.abc import Hashable
    new_arr = set([el for el in arr if isinstance(el, Hashable)])
    print(new_arr)

n = 1
while n != 0:
    n = int(input("Введите номер задания (1-4, 0 - выход)\n> "))
    
    match n:
        case 0:
            pass
        case 1:
            numbers = input("Введите элементы кортежа ч-з пробел\n> ").strip()
            numbers = numbers.split()
            First_Task(numbers)

        case 2:
            numbers = input("Введите элементы кортежа ч-з пробел\n> ").strip()
            element = input("Введите требуемый элемента для среза\n>")
            numbers = numbers.split()
            Second_Task(tuple(n for n in numbers), element)

        case 3:
            inp = input("Введите строку/числа (чз пробел)\n> ").strip().split()
            Fourth_Task(inp)