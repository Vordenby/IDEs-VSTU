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
    ind = [i for i in range(len(cort)) if cort[i] == el]
    if len(ind) == 0:
        print(())
    elif len(ind) == 1:
        print(cort[ind[0]:])
    else:
        print(cort[ind[0]:ind[1]+1])

def Third_Task(arr):
    res = set(arr)
    print(f"Множество: {res}, мощность: {len(res)}.")

def Fourth_Task(arr):
    from collections.abc import Hashable
    new_arr = set([el for el in arr if isinstance(el, Hashable)])
    print(new_arr)

n = 1
while n != 0:
    n = int(input("Введите номер задания (1-4, 0 - выход).\n> "))
    
    match n:
        case 0:
            pass
        case 1:
            numbers = input("Введите элементы кортежа ч-з пробел.\n> ").strip().split()
            First_Task(numbers)

        case 2:
            numbers = input("Введите элементы кортежа ч-з пробел.\n> ").strip().split()
            element = input("Введите требуемый элемента для среза.\n>")
            Second_Task(tuple(n for n in numbers), element)

        case 3:
            inp = input("Введите строку/числа ч-з пробел.\n> ").strip().split()
            Third_Task(inp)
        case 4:
            inp = input("Введите элементы ч-з пробел.\n> ").strip().split()
            Fourth_Task(inp)
        case _:
            print("Выбран неверный вариант.")
