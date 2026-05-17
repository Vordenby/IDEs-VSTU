import csv
import json


class NoSuchCountryError(Exception):
    def __init__(self, message):
        super().__init__(message)


class IllegalArgumentError(ValueError):
    pass


class NoSuchFieldError(Exception):
    def __init__(self, message):
        super().__init__(message)


def load_data(filename):
    with open(filename, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        data = []
        if reader.fieldnames is None:
            return data

        for row in reader:
            if not row:
                continue

            keys = [key for key in row.keys() if key]
            if not keys:
                continue

            # Определение ключа для названия страны
            name_key = next(
                (key for key in keys if key.strip().lower() in
                 ("country name", "country", "name", "countryname")),
                keys[0],
            )

            # Определение ключа для ВВП - выбираем последний числовой ключ
            gdp_key = None
            numeric_keys = [
                key for key in keys
                if key.strip().lower() not in (
                    "country", "country name", "name", "countryname",
                    "series name", "series code", "country code",
                    "indicator name", "indicator code",
                )
            ]
            if numeric_keys:
                gdp_key = numeric_keys[-1]
            elif len(keys) > 1:
                gdp_key = keys[-1]
            else:
                gdp_key = keys[0]

            country = row.get(name_key, "").strip()
            gdp_value = row.get(gdp_key, "").strip()
            
            # Пропускаем строки с отсутствующими значениями
            if not country or not gdp_value:
                continue

            try:
                gdp = float(gdp_value.replace(',', '.'))
            except ValueError:
                continue

            data.append({"name": country, "gdp": gdp})

    return data


def search(data, criteria):
    if not data:
        raise NoSuchCountryError("Данные не содержат стран с известным ВВП.")

    # Определение операции
    if criteria == "-max-":
        return max(data, key=lambda item: item["gdp"])
    elif criteria == "-min-":
        return min(data, key=lambda item: item["gdp"])
    else:
        # Поиск по названию страны
        for item in data:
            if item["name"].lower() == criteria.lower():
                return item

        raise NoSuchCountryError(
            "Значение параметра 'criteria' может быть "
            "одним из:\n"
            '- "-max-": государство с максимальным ВВП на душу населения;\n'
            '- "-min-": государство с мнимальным ВВП на душу населения;\n'
            '- "Russian Federation": название государства.')


def save_data(filename, data, criteria):
    try:
        method, value = criteria.split("=", 1)
    except ValueError:
        raise IllegalArgumentError(
            "Значение параметра 'criteria' может быть "
            "одним из:\n"
            '- "top=X": первые X государств по ВВП на душу населения'
            ' (целое число > 0, по убыванию значения);\n'
            '- "tail=X": последние X государств по ВВП на душу населения'
            ' (целое число > 0, по возрастанию значения);\n'
            '- "greater=X": список государств с ВВП на душу населения, больше'
            ' чем X (вещ. число, по убыванию значения);\n'
            '- "less=X": список государств с ВВП на душу населения, меньше'
            ' чем X (вещ. число, по возрастанию значения).')

    filtered_data = []
    
    # Определение операции
    if method == "top":
        limit = int(value)
        if limit <= 0:
            raise ValueError("Значение должно быть > 0")
        filtered_data = sorted(data, key=lambda item: item["gdp"], reverse=True)[:limit]
    elif method == "tail":
        limit = int(value)
        if limit <= 0:
            raise ValueError("Значение должно быть > 0")
        filtered_data = sorted(data, key=lambda item: item["gdp"])[:limit]
    elif method == "greater":
        threshold = float(value)
        filtered_data = [
            item for item in sorted(data, key=lambda item: item["gdp"], reverse=True)
            if item["gdp"] > threshold
        ]
    elif method == "less":
        threshold = float(value)
        filtered_data = [
            item for item in sorted(data, key=lambda item: item["gdp"])
            if item["gdp"] < threshold
        ]
    else:
        raise ValueError("Неизвестная операция")

    # Сохранение в файл
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "gdp"])
        writer.writeheader()
        for item in filtered_data:
            writer.writerow({"name": item["name"], "gdp": item["gdp"]})


def FF_Task():
    def WriteBack(nums):
        with open("FF_task.txt", "w") as f:
            f.write(" ".join(map(str, nums)))    
    
    nums = []
    x = 1.0
    print("Вводите числа (0 - остановка)")
    while x != 0:
        x = float(input("> "))
        if x != 0:
            nums.append(x)
    WriteBack(nums)


def FS_Task():
    with open("FS_task.txt", "r") as f:
        content = f.read()
        mx = 0
        sm = 0
        for num in content.split():
            mx = max(float(num), mx)
            sm = sm + float(num)
    with open("FS_task.txt", "w") as f:
        f.write(f"{mx}\n{sm}")


def FT_Task():
    with open("FT_task.txt", "r") as f:
        content = f.read()
    values = []
    for t in content.split():
        try:
            values.append(float(t))
        except ValueError:
            continue
    mx = max(values) if values else 0
    sm = sum(values)

    with open("FT_task.txt", "w") as f:
        f.write(f"{mx}\n{sm}")


def FN_Task():
    alphabet_v = "аеёиоуыэюя"
    alphabet_c = "бвгджзклмнпрстфхцчшщ"

    name = input("Введите имя файла: ")
    with open(name, "r") as f:
        content = f.read()

    print(content)
    words = content.split()
    for x in words:
        vowel_words = sum(1 for char in x if char in alphabet_v)
        consonant_words = sum(1 for char in x if char in alphabet_c)
        print(f"{x}: гласных - {vowel_words}, согласных - {consonant_words}")


def FB_Task():
    filename = input("Введите имя файла: ")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            t = f.read().split()
    except FileNotFoundError:
        print("Файл не найден.")
        return

    total = len(t)
    if total == 0:
        print("Файл пуст.")
        return

    counts = {}
    spoiled = 0
    for token in t:
        try:
            num = int(token)
        except ValueError:
            spoiled += 1
            continue

        if num == -1:
            spoiled += 1
        elif num >= 1:
            counts[num] = counts.get(num, 0) + 1
        else:
            spoiled += 1

    results = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    for index, (party, votes) in enumerate(results, start=1):
        percent = votes / total * 100 if total else 0
        print(f"{index}. Партия №{party} | {votes} | {percent:.2f}%")

    if spoiled > 0:
        print(f"Испорченных бланков: {spoiled}")


def SF_Task():
    print("Задача SF: анализ ВВП на душу населения")
    try:
        filename = input("Введите имя файла: ")
        save_filename = input("Введите имя файла для сохранения: ")
        
        data = load_data(filename)
        print(f"Загружено стран с известным ВВП: {len(data)}")
        
        # Поиск максимума
        max_country = search(data, criteria="-max-")
        print(f"Максимум ВВП: {max_country}")
        
        # Поиск минимума
        min_country = search(data, criteria="-min-")
        print(f"Минимум ВВП: {min_country}")
        
        # Поиск по названию
        try:
            rf_data = search(data, criteria="Russian Federation")
            print(f"Russian Federation: {rf_data}")
        except NoSuchCountryError:
            print("Russian Federation не найдена в данных")
        
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
    choice = input("Выберите задание (1 - FF_Task, 2 - FS_Task, 5 - FB_Task, 9 - SF_Task): ")
    try:
        if choice == "1":
            FF_Task()
        elif choice == "2":
            FS_Task()
        elif choice == "5":
            FB_Task()
        elif choice == "9":
            SF_Task()
        else:
            print("Неверный выбор задания.")
    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
    except Exception as err:
        print(f"Ошибка при выполнении задания: {err}")
