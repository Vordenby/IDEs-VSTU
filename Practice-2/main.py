from math import *

def FirstTask(a, b):
    print("a + b =", a+b)
    print("a - b =", a-b)
    print("a * b =", a*b)
    print("a / b =", a/b)
    print("a // b =", a//b)
    print("a '%' b =", a%b)
    print("a**b =", a**b)
    print("a < b =", a<b)
    print("a <= b", a<=b)
    print("a > b", a>b)
    print("a >= b", a>=b)
    print("a != b", a!=b)
    print("a == b", a==b)

def SecondTask(x,y,z):
    x, y, z = map(int, input("Введите x y z (чз пробел)").split())
    
    numerator = pow(((x**5)+9)/(fabs(-8) * y), 1/3)
    denumerator = 7 - z*modf(y)
    return numerator/denumerator

def ThirdTask(R1, R2):
    return R1+R2

def FourthTask(a, b):
    def Findres(a):
        sum = 0, pr = 1
        for i in f"{a}":
            sum+=int(i)
            pr*=int(i)
        return [sum, pr]
    A = Findres(a)
    B = Findres(b)
    print(f"{a}-->{A[0]}-->{A[1]}")
    print(f"{b}-->{B[0]}-->{B[1]}")