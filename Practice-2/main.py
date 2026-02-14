from math import *

def FirstTask(a, b):
    print("a + b =", a+b)
    print("a - b =", a-b)
    print("a * b =", a*b)
    print("a / b =", round(a/b, 2))
    print("a // b =", a//b)
    print("a '%' b =", round(a%b, 2))
    print("a**b =", a**b)
    print("a < b =", a<b)
    print("a <= b", a<=b)
    print("a > b", a>b)
    print("a >= b", a>=b)
    print("a != b", a!=b)
    print("a == b", a==b)

def SecondTask(x,y,z):    
    numerator = pow(((x**5)+9)/(fabs(-8) * y), 1/3)
    denumerator = 7 - z*(y % 1)
    
    if denumerator == 0:
        print("Деление на ноль!")
        return None
   
    return round(numerator/denumerator, 3)

def ThirdTask(R1, R2):
    if not(R1>0 and R2>0):
        print("Значения(е) были(о) отрицательны(ое)")
        return None
    return round(R1+R2, 1)
        

def FourthTask(a, b):

    a = abs(a)
    b = abs(b)

    def Findres(a):

        sum = 0
        pr = 1

        for i in f"{a}":
            sum+=int(i)
            pr*=int(i)
        return [sum, pr]
    
    A = Findres(a)
    B = Findres(b)

    print(f"{a}-->{A[0]}-->{A[1]}")
    print(f"{b}-->{B[0]}-->{B[1]}")

def FifthTask(minutes):
    
    full_hours = minutes // 60
    count_of_mins = minutes % 60

    return [full_hours, count_of_mins]

def SixthTask(a, b, c, m, n):
    
    D = (b**2) - 4*a*c
    
    if D < 0:
        return False
        
    elif D == 0:
        x = -b / (2*a)
        return m <= x <= n
        
    else:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        return (m <= x1 <= n) or (m <= x2 <= n)




ch = 1

while ch != 0:
    
    ch = int(input("Выберите задание (1 - 6, 0 - выход)\n> "))
    
    match ch:

        case 1:
            a, b = map(int, input("Введите a b (чз пробел)\n> ").split())
            FirstTask(a, b)
        
        case 2:
            x, y, z = map(int, input("Введите x y z (чз пробел)\n> ").split())
            print(f"Полученное значение: {SecondTask(x,y,z)}")

        case 3:
            R1, R2 = map(float, input("Введите a b (чз пробел)\n> ").split())
            print(f"Полученное сопротивление: {ThirdTask(R1, R2)}")

        case 4:
            a, b = map(int, input("Введите 2-значное и 3-значное (чз пробел)\n> ").split())
            FourthTask(a, b)

        case 5:
            min = int(input("Введите кол-во минут\n> "))
            res = FifthTask(min)
            print(f"Полных часов: {res[0]}\nколичество минут, \nпрошедших с момента начала\n последнего часа: ${res[1]}")

        case 6:
            a, b, c = map(float, input("Введите a b c квадратного уравнения (чз пробел)\n> ").split())
            m, n = map(float, input("Введите интервал m n (чз пробел)\n> ").split())
            if SixthTask(a, b, c, m, n):
                print("Решение уравнения попадает в указанный отрезок!")
            else:
                print("Решение уравнения не попадает в указанный отрезок.")

        case _:
            print("Неверное значение!")