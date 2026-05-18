import csv
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def local_path(filename):
    return os.path.join(SCRIPT_DIR, filename)


import csv


class NoSuchCountryError(Exception):
    def __init__(self, message):
        super().__init__(message)


class IllegalArgumentError(ValueError):
    pass


class NoSuchFieldError(Exception):
    def __init__(self, message):
        super().__init__(message)


def _parse_number(value: str) -> float:
    value = value.strip().replace("\xa0", "").replace(" ", "")
    if "," in value and "." not in value:
        value = value.replace(",", ".")
    else:
        value = value.replace(",", "")
    return float(value)


def load_data(filename):
    with open(local_path(filename), encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))

    header_idx = next(
        (i for i, row in enumerate(rows) if row and row[0].strip() == "Country Name"),
        None,
    )
    if header_idx is None:
        return []

    header = rows[header_idx]
    data = []

    for row in rows[header_idx + 1:]:
        if not row or not any(cell.strip() for cell in row):
            continue

        if len(row) < len(header):
            row = row + [""] * (len(header) - len(row))

        country = row[0].strip()
        if not country:
            continue

        gdp = None
        for cell in reversed(row[4:]):
            cell = cell.strip()
            if not cell:
                continue
            try:
                gdp = _parse_number(cell)
                break
            except ValueError:
                continue

        if gdp is not None:
            data.append({"name": country, "gdp": gdp})

    return data


def search(data, criteria):
    if not data:
        raise NoSuchCountryError("Данные не содержат стран с известным ВВП.")

    if criteria == "-max-":
        return max(data, key=lambda item: item["gdp"])
    if criteria == "-min-":
        return min(data, key=lambda item: item["gdp"])

    for item in data:
        if item["name"].lower() == criteria.lower():
            return item

    raise NoSuchCountryError(
        "Значение параметра 'criteria' может быть "
        "одним из:\n"
        '- "-max-": государство с максимальным ВВП на душу населения;\n'
        '- "-min-": государство с минимальным ВВП на душу населения;\n'
        '- "Russian Federation": название государства.'
    )


def save_data(filename, data, criteria):
    try:
        method, value = criteria.split("=", 1)
    except ValueError:
        raise IllegalArgumentError(
            "Значение параметра 'criteria' может быть "
            "одним из:\n"
            '- "top=X": первые X государств по ВВП на душу населения '
            '(целое число > 0, по убыванию значения);\n'
            '- "tail=X": последние X государств по ВВП на душу населения '
            '(целое число > 0, по возрастанию значения);\n'
            '- "greater=X": список государств с ВВП на душу населения, больше '
            'чем X (вещественное число, по убыванию значения);\n'
            '- "less=X": список государств с ВВП на душу населения, меньше '
            'чем X (вещественное число, по возрастанию значения).'
        )

    method = method.strip()
    value = value.strip()

    if method == "top":
        try:
            limit = int(value)
        except ValueError:
            raise IllegalArgumentError("top должен быть целым числом > 0")
        if limit <= 0:
            raise IllegalArgumentError("top должен быть целым числом > 0")
        filtered_data = sorted(data, key=lambda item: item["gdp"], reverse=True)[:limit]

    elif method == "tail":
        try:
            limit = int(value)
        except ValueError:
            raise IllegalArgumentError("tail должен быть целым числом > 0")
        if limit <= 0:
            raise IllegalArgumentError("tail должен быть целым числом > 0")
        filtered_data = sorted(data, key=lambda item: item["gdp"])[:limit]

    elif method == "greater":
        try:
            threshold = float(value)
        except ValueError:
            raise IllegalArgumentError("greater должен быть вещественным числом")
        filtered_data = [
            item for item in sorted(data, key=lambda item: item["gdp"], reverse=True)
            if item["gdp"] > threshold
        ]

    elif method == "less":
        try:
            threshold = float(value)
        except ValueError:
            raise IllegalArgumentError("less должен быть вещественным числом")
        filtered_data = [
            item for item in sorted(data, key=lambda item: item["gdp"])
            if item["gdp"] < threshold
        ]

    else:
        raise IllegalArgumentError(
            "Значение параметра 'criteria' может быть "
            "одним из:\n"
            '- "top=X": первые X государств по ВВП на душу населения '
            '(целое число > 0, по убыванию значения);\n'
            '- "tail=X": последние X государств по ВВП на душу населения '
            '(целое число > 0, по возрастанию значения);\n'
            '- "greater=X": список государств с ВВП на душу населения, больше '
            'чем X (вещественное число, по убыванию значения);\n'
            '- "less=X": список государств с ВВП на душу населения, меньше '
            'чем X (вещественное число, по возрастанию значения).'
        )

    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "gdp"])
        writer.writeheader()
        writer.writerows(filtered_data)


def FF_Task():

    def WriteBack(nums):
        with open(local_path("FF_task.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(str(num) for num in nums))    
    
    nums = []
    x = 1.0
    print("Вводите числа (0 - остановка)")
    while x != 0:
        x = float(input("> "))
        if x != 0:
            nums.append(x)
    WriteBack(nums)


def FS_Task():
    try:
        with open(local_path("FF_task.txt"), "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("Ошибка: файл FF_task.txt не найден.")
        return

    mx = 0
    sm = 0
    for num in content.split():
        mx = max(float(num), mx)
        sm = sm + float(num)

    with open(local_path("FF_task.txt"), "a", encoding="utf-8") as f:
        f.write(f"\n{mx}\n{sm}")


def FT_Task():
    try:
        with open(local_path("FF_task.txt"), "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("Ошибка: файл FF_task.txt не найден.")
        return

    values = []
    for t in content.split():
        try:
            values.append(float(t))
        except ValueError:
            continue
    mx = max(values) if values else 0
    sm = sum(values)

    with open(local_path("FF_task.txt"), "a", encoding="utf-8") as f:
        f.write(f"\n{mx}\n{sm}")


def FN_Task():
    alphabet_v = "аеёиоуыэюя"
    alphabet_c = "бвгджзклмнпрстфхцчшщ"

    name = input("Введите имя файла: ")
    with open(local_path(name), "r") as f:
        content = f.read()

    print("Стих: \n\n" + content + "\n")
    words = content.split()
    vow = 0
    cons = 0
    for x in words:
        if x[0].lower() in alphabet_v:
            vow += 1
        elif x[0].lower() in alphabet_c:
            cons += 1
    print(f"Гласных: {vow}\nСогласных: {cons}")        
    print("Гласных больше\n") if vow > cons else print("Согласных больше\n") if cons > vow else print("Гласных и согласных поровну\n")


def FB_Task():
    filename = input("Введите имя файла: ")
    try:
        with open(local_path(filename), "r", encoding="utf-8") as f:
            t = f.read().split()
    except FileNotFoundError:
        print("Файл не найден.")
        return

    total = len(t)
    if total == 0:
        print("Файл пуст.")
        return

    parties = ["Партия №1", "Партия №2", "Партия №3", "Партия №4", "Партия №5"]
    corrupted = sum([int(x) for x in t[4:] if x.isdigit()])
    votes = sum([int(x) for x in t if x.isdigit()])    
    parties_votes = [int(x) if x.isdigit() else 0 for x in t[:len(parties)]]
    party_pairs = list(zip(parties, parties_votes))

    party_pairs.sort(key=lambda p: p[1], reverse=True)

    print(f"Всего бюллетеней: {votes}")
    
    w_votes = max(len(str(v)) for _, v in party_pairs)
    for idx, (name, v) in enumerate(party_pairs, start=1):
        pct = (v / votes) * 100 if votes else 0
        print(f"{idx}. {name} | {str(v).rjust(w_votes)} | {pct:6.2f}%")
    print(f"Испорченных бюллетеней: {corrupted} ({(corrupted / votes) * 100:.2f}%)")

def SF_Task():
    print("Анализ ВВП на душу населения")
    try:
        filename = input("Введите имя файла: ")
        save_filename = input("Введите имя файла для сохранения: ")
        
        data = load_data(filename)
        print(f"Загружено стран с известным ВВП: {len(data)}")
        
        max_country = search(data, criteria="-max-")
        print(f"Максимум ВВП: {max_country}")
        
        min_country = search(data, criteria="-min-")
        print(f"Минимум ВВП: {min_country}")
        
        try:
            rf_data = search(data, criteria="Российская Федерация")
            print(f"Российская Федерация: {rf_data}")
        except NoSuchCountryError:
            print("Российская Федерация не найдена в данных")
        
        save_data(save_filename, data, criteria="top=10")
        print(f"Данные сохранены в файл: {save_filename}")
        
    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
    except NoSuchCountryError as err:
        print(f"Ошибка: {err}")
    except IllegalArgumentError as err:
        print(f"Ошибка: {err}")
    except Exception as err:
        print(f"Непредвиденная ошибка: {err}")


if __name__ == "__main__":
    while True:
        choice = input("Выберите задание \n1 - Задание 1.1\n2 - Задание 1.2\n3 - Задание 1.3\n4 - Задание 1.4\n5 - Задание 1.5\n6 - Задание 2.1\n0 - Выйти\n\n> ")
        try:
            if choice == "1":
                FF_Task()
            elif choice == "2":
                FS_Task()
            elif choice == "3":
                FT_Task()
            elif choice == "4":
                FN_Task()
            elif choice == "5":
                FB_Task()
            elif choice == "6":
                SF_Task()
            elif choice == "0":
                print("Выход из программы...")
                break
            else:
                print("Неверный выбор задания.")
        except FileNotFoundError:
            print("Ошибка: Файл не найден.")
        except Exception as err:
            print(f"Ошибка при выполнении задания: {err}")
