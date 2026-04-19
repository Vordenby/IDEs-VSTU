from math import *
from statistics import *

def First_Task_A(x):

    if x >= 0:
        return sqrt(x) + pow(x, 2)
    else:
        return 1/x
    
def First_Task_B():
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    
    if num1 > num2:
        print(f"Максимальное: {num1}, Минимальное: {num2}")
    elif num2 > num1:
        print(f"Максимальное: {num2}, Минимальное: {num1}")
    else:
        print("Числа равны.")


def Second_Task_A():

    x = 1
    k = 0
    sm = 0

    while x !=0:
        x = int(input())
        k+=1
        sm += x

    print(f'Сумма: {sm}, кол-во чисел: {k}')

def Second_Task_B(n):

    DL = [x for x in range(0, n, 5)]
    print(f"Числа, которые не превышают {n}: {DL}")

def Third_Task_A(a, b):

    if a > b:
        print([x for x in range(b, a)])
    else:
        print([x for x in range(a, b)])

def Third_Task_B(arr, p):

    if sum(arr) > p:
        print("Перевозка груза невозможна.")
    else:
        print("Перевозка груза возможна.")

def Fourth_Task():
    x = 1
    k = 0
    sm = 0

    while True:
        x = int(input())
        if x == 0:
            break
        k+=1
        sm += x
    
    print(f'Сумма: {sm}, кол-во чисел: {k}')

def Fifth_Task(a, b, c):
    
    for i in range(a, b):
        if i % c == 0:
            print(i)

def Sixth_Task_A(arr):

    def geom(arr):

        arr = [abs(n) for n in arr]

        return prod(arr) ** (1/len(arr))

    arr_plus = [x for x in arr if x >= 0]
    
    arr_minus = []
    
    for x in arr:
        if x < 0:
            arr_minus.append(x)
    
    print(f"{arr}\nПоложительные: {arr_plus}\nОтрицательные: {arr_minus}\nСреднее арифметического 1-го списка: {mean(arr_plus)}]\nСреднее геометрическое 2-го списка: {geom(arr_minus)}")

def Sixth_Task_B(arr):
    
    IsAllPlus = True
    IsNull = False
    IsChet = True
    IsNeChet = False

    for x in arr:
        if x == 0:
            IsNull = True
            break

    for x in arr:
        if x < 0:
            IsAllPlus = False
            break
    for x in arr:
        if x % 2 != 0:
            IsChet = False
            IsNeChet = True
            break
    
    print(f"Все элементы положительны: {IsAllPlus}, {all(x >= 0 for x in arr)}")
    print(f"Хотя бы один нулевой элемент: {IsNull}, {any(x == 0 for x in arr)}")
    print(f"Все элементы четные: {IsChet}, {all(x % 2 == 0 for x in arr)}")
    print(f"Хотя бы один нечетный элемент: {IsNeChet}, {any(x % 2 != 0 for x in arr)}")

def Sixth_Task_C(msg, a):

    msg = msg.split()

    n_msg = [x +' ' for x in msg if a.lower() not in x.lower()]

    print(''.join(n_msg))

while True:
    print("="*30)
    print("1. Задание 1.1 (Функция f(x))")
    print("2. Задание 1.2 (Макс/Мин)")
    print("3. Задание 2.1 (Сумма и количество чисел)")
    print("4. Задание 2.2 (Числа, не превышающие n)")
    print("5. Задание 3.1 (Диапазон чисел)")
    print("6. Задание 3.2 (Грузовик)")
    print("7. Задание 4 (Бесконечный цикл)")
    print("8. Задание 5 (Числа, кратные c)")
    print("9. Задание 6.1 (Списки: положительные/отрицательные)")
    print("10. Задание 6.2 (Проверки списка)")
    print("11. Задание 6.3 (Фильтр слов)")
    print("0. Выход")
    print("="*30)
    choice = input("Введите номер задачи: ")
    
    match choice:
        case "1":
            try:
                x = float(input("Введите значение x: "))
                print(f"Результат: {First_Task_A(x)}")
            except ValueError:
                print("Ошибка: введите число.")
        
        case "2":
            First_Task_B()

        case "3":
            Second_Task_A()
        case "4":
            try:
                n = int(input("Введите число n: "))
                Second_Task_B(n)
            except ValueError:
                print("Ошибка: введите целое число.")
        case "5":
            try:
                a = int(input("Введите начало диапазона a: "))
                b = int(input("Введите конец диапазона b: "))
                Third_Task_A(a, b)
            except ValueError:
                print("Ошибка: введите целые числа.")
        case "6":
            try:
                arr_input = input("Введите массы предметов через пробел: ")
                arr = list(map(float, arr_input.split()))
                p = float(input("Введите грузоподъемность p: "))
                Third_Task_B(arr, p)
            except ValueError:
                print("Ошибка: введите числа.")
        case "7":
            Fourth_Task()
        case "8":
            try:
                a = int(input("Введите начало a: "))
                b = int(input("Введите конец b: "))
                c = int(input("Введите число c: "))
                Fifth_Task(a, b, c)
            except ValueError:
                print("Ошибка: введите целые числа.")
        case "9":
            try:
                arr_input = input("Введите список чисел через пробел: ")
                arr = list(map(float, arr_input.split()))
                Sixth_Task_A(arr)
            except ValueError:
                print("Ошибка: введите числа.")
        case "10":
            try:
                arr_input = input("Введите список чисел через пробел: ")
                arr = list(map(int, arr_input.split()))
                Sixth_Task_B(arr)
            except ValueError:
                print("Ошибка: введите числа.")
        case "11":
            msg = input("Введите предложение: ")
            a = input("Введите букву для удаления: ")
            Sixth_Task_C(msg, a)
        case "0":
            break
        case _:
            print("Неверный выбор.")