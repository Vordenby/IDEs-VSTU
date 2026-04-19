
# Задание 1
def ceasar(text, shift):
    """Вернуть измененную строку 'text' со сдвигом 'shift'.

    Параметры:
        - text (str): строка;
        - shift (int): сдвиг.

    Результат:
        str: измененная строка."""
    
    letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]

    result = ""
    for char in text:
        if char.lower() in letters:
            index = letters.index(char.lower())
            new_index = (index + shift) % len(letters)
            if char.isupper():
                result += letters[new_index].upper()
            else:
                result += letters[new_index]
        else:
            result += char
    
    return result

# Задание 2
def power(x, y=2):
    """Вернуть x^y."""
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)

# Задание 3

n = int(input("Введите кол-во человек: "))

middle_names = {}
for i in range(n):
    fio = input("Введите ФИО через пробел: ").split()

    middle_name = fio[2]
    middle_names[middle_name] = middle_names.get(middle_name, 0) + 1

print(sorted(middle_names.items(), key=lambda item: item[1])[-1][0])
print("В расчете участвовало человек:", n)

#Задание 4

необходимые_экзамены = {
    "Информатика": 80,
    "Математика": 85,
    "Русский язык": 75
}

print("""Для определения возможности поступления, необходима информация о Вас.

Для ввода экзамена и баллов введите их через |: Химия | 40.
Для завершения ввода нажмите Enter.
""")

сданные_экзамены = {}
while True:
    ввод = input("").strip()
    if ввод == "":
        break

    экзамен, балл = [x.strip() for x in ввод.split("|")]
    сданные_экзамены[экзамен] = int(балл)

print("Ваши экзамены:")
for i, (экзамен, балл) in enumerate(сданные_экзамены.items(), start=1):
    print("{}) {} {}".format(i, экзамен, балл))

ok = False
for необходимый_экзамен, баллы in необходимые_экзамены.items():
    if сданные_экзамены[необходимый_экзамен] < баллы:
        break
else:
    ok = True

print("Вы можете к нам поступить!" if ok else "Увы...")

