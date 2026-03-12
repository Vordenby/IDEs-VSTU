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

n = 1
while n != 0:
    n = int(input("Введите номер задания (1-4, 0 - выход)\n> "))
    
    match n:
        case 0:
            pass
        case 1:
            numbers = input("Введите значения ч-з пробел\n> ").strip()
            numbers = numbers.split()
            First_Task(numbers)
        