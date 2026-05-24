def first_task(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        print("Стороны должны быть положительными")
    elif a + b > c and a + c > b and b + c > a:
        print("Треугольник можно построить")
        if a == b == c:
            print("Треугольник равносторонний")
        elif a == b or b == c or a == c:
            print("Треугольник равнобедренный")
        else:
            print("Треугольник обычный")
    else:
        print("Треугольник построить нельзя")

def second_task(x,y):
    print(f"x = {x}, y = {y}")
    x,y = y,x
    print(f"x = {x}, y = {y}")

def third_task():
    a = []
    while not [0, 0, 0] in a:
        x = int(input("> "))
    print(sum(a))
