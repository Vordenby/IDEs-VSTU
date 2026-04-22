
from __future__ import annotations

from typing import Dict


class NoMoneyToWithdrawError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class PaymentError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


def caesar(text: str, shift: int) -> str:

    lower = [chr(i) for i in range(ord("а"), ord("я") + 1)]
    upper = [chr(i) for i in range(ord("А"), ord("Я") + 1)]

    def shift_char(ch: str) -> str:
        if ch in lower:
            idx = lower.index(ch)
            return lower[(idx + shift) % len(lower)]
        if ch in upper:
            idx = upper.index(ch)
            return upper[(idx + shift) % len(upper)]
        return ch

    return "".join(shift_char(ch) for ch in text)


def power(x, y=2):
    if not isinstance(y, int):
        raise TypeError("Показатель степени должен быть целым числом.")
    if y == 0:
        return 1
    if y < 0:
        if x == 0:
            raise ZeroDivisionError("0 нельзя возводить в отрицательную степень.")
        return 1 / power(x, -y)
    return x * power(x, y - 1)


def task1() -> None:
    print("Задание 1. Шифр Цезаря")
    try:
        text = input("Введите предложение: ")
        shift = int(input("Введите сдвиг: "))
        encoded = caesar(text, shift)
        decoded = caesar(encoded, -shift)
        print("Зашифрованная строка:", encoded)
        print("Расшифрованная строка:", decoded)
    except ValueError:
        print("Ошибка ввода: сдвиг должен быть целым числом.")


def task2() -> None:
    print("Задание 2. Возведение в степень")
    try:
        x = int(input("x="))
        y = int(input("y="))
        print("Результат:", power(x, y))
    except ValueError:
        print("Ошибка ввода: x и y должны быть целыми числами.")
    except ZeroDivisionError as exc:
        print("Ошибка:", exc)
    except TypeError as exc:
        print("Ошибка:", exc)


def task3() -> None:
    print("Задание 3. Наиболее частое отчество")
    try:
        n = int(input("Введите кол-во человек: "))
        middle_names: Dict[str, int] = {}

        for i in range(n):
            fio = input("Введите ФИО через пробел: ").split()
            try:
                middle_name = fio[2]
            except IndexError:
                print("  ФИО без отчества пропущено.")
                continue
            middle_names[middle_name] = middle_names.get(middle_name, 0) + 1

        if not middle_names:
            print("Отчества не найдены.")
        else:
            most_common = max(middle_names, key=middle_names.get)
            print(most_common)
        print("В расчете участвовало человек:", n)
    except ValueError:
        print("Ошибка ввода: количество человек должно быть целым числом.")


def task4() -> None:
    print("Задание 4. Проверка возможности поступления")
    необходимые_экзамены = {
        "Информатика": 80,
        "Математика": 85,
        "Русский язык": 75,
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
        try:
            экзамен, балл = [x.strip() for x in ввод.split("|", 1)]
            сданные_экзамены[экзамен] = int(балл)
        except ValueError:
            print("  Неверный формат. Используйте: Предмет | Баллы")
        except Exception as exc:
            print("  Ошибка ввода:", exc)

    print("Ваши экзамены:")
    for i, (экзамен, балл) in enumerate(сданные_экзамены.items(), start=1):
        print("{}) {} {}".format(i, экзамен, балл))

    ok = True
    try:
        for необходимый_экзамен, баллы in необходимые_экзамены.items():
            if сданные_экзамены[необходимый_экзамен] < баллы:
                ok = False
                break
    except KeyError:
        ok = False

    print("Вы можете к нам поступить!" if ok else "Увы...")


def print_accounts(accounts: Dict[str, int]) -> None:
    print("Список клиентов ({}): ".format(len(accounts)))
    for i, (name, value) in enumerate(accounts.items(), start=1):
        print("{}. {} {}".format(i, name, value))


def transfer_money(accounts: Dict[str, int], account_from: str, account_to: str, value: int) -> None:
    snapshot = accounts.copy()

    try:
        if value <= 0:
            raise PaymentError("Сумма перевода должна быть положительной.")
        if account_from not in accounts:
            raise PaymentError(f"Счет '{account_from}' не найден.")
        if account_to not in accounts:
            raise PaymentError(f"Счет '{account_to}' не найден.")
        if accounts[account_from] < value:
            raise NoMoneyToWithdrawError(
                f"На счету '{account_from}' недостаточно денег для перевода."
            )

        accounts[account_from] -= value
        accounts[account_to] += value

    except NoMoneyToWithdrawError:
        accounts.clear()
        accounts.update(snapshot)
        raise
    except Exception as exc:
        accounts.clear()
        accounts.update(snapshot)
        if isinstance(exc, PaymentError):
            raise
        raise PaymentError("Ошибка при переводе.") from exc


def task5() -> None:
    print("Задание 5. Перевод денег с транзакцией")
    accounts = {
        "Василий Иванов": 100,
        "Екатерина Белых": 1500,
        "Михаил Лермонтов": 400,
    }
    print_accounts(accounts)

    payment_info = {
        "account_from": "Екатерина Белых",
        "account_to": "Василий Иванов",
    }

    print("Перевод от {account_from} для {account_to}...".format(**payment_info))

    try:
        payment_info["value"] = int(input("Сумма = "))
        transfer_money(accounts, **payment_info)
        print("OK!")
        print_accounts(accounts)
    except ValueError:
        print("Ошибка ввода: сумма должна быть целым числом.")
    except NoMoneyToWithdrawError as exc:
        print("Ошибка:", exc)
        print_accounts(accounts)
    except PaymentError as exc:
        print("Ошибка:", exc)
        print_accounts(accounts)


def menu() -> None:
    actions = {
        "1": task1,
        "2": task2,
        "3": task3,
        "4": task4,
        "5": task5,
    }

    while True:
        print(
            """
Меню:
1 - Задание 1 (шифр Цезаря)
2 - Задание 2 (power)
3 - Задание 3 (отчество)
4 - Задание 4 (поступление)
5 - Задание 5 (перевод денег)
0 - Выход
"""
        )
        choice = input("Выберите задание: ").strip()
        if choice == "0":
            print("Выход.")
            break
        action = actions.get(choice)
        if action is None:
            print("Неверный выбор. Попробуйте еще раз.")
            continue
        action()


if __name__ == "__main__":
    menu()
