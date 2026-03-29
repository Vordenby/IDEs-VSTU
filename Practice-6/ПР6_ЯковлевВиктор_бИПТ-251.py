info = {}

info["фио"] = "Яковлев Виктор Александрович"
info["дата_рождения"] = "20.10.2006"
info["место_рождения"] = "Старый Оскол"

print(info)

hobbies = ["Фотоохота, Программирование, Игры, Шахматы, Чтение"]
pets = ["кошка Плюша", "собака Валли", "собака Марта"]

info["хобби"] = hobbies
info["животные"] = pets

Ege = {}
Ege["Математика"] = 58
Ege["Информатика"] = 80
Ege["Русский язык"] = 67

Ege["Физика"] = 70
del Ege["Физика"]

info["ЕГЭ"] = Ege

info["ВУЗы"] = {}

iau = {}

iau["ВГТУ"] = 192
iau["ВГУ"] = 224
iau["МГТУ им. Баумана"] = 284
iau["ИТМО"] = 254
iau["РТУ МИРЭА"] = 217
iau["МТУСИ"] = 190

info["ВУЗы"] = iau

print("\nДанные:", info)
print("\nПредметы:", sorted(info["ЕГЭ"].keys()))
print("\nВУЗы:", sorted(info["ВУЗы"].keys()))

print("\nОтветы на вопросы\n")
name = info["фио"][7:14]

starts_with_vowel = name[0].lower() in "аеёийоуэюя"

print("* мое имя начинается на гласную букву:", starts_with_vowel)

month = info["дата_рождения"][3:5]

born_in_winter_or_summer = int(month) in [6, 7, 8, 12, 1, 2]

print("* родился летом или зимой:", born_in_winter_or_summer)

hobbies_count = len(hobbies)

print("* у меня {} хобби, первое {}".format(hobbies_count, hobbies[0]))

print("* после окончания школы сдавал {} экз.".format(len(Ege)))


sum_mark = sum([Ege[x] for x in Ege])

print("* сумма баллов = {}".format(sum_mark))

max_mark = max([Ege[x] for x in Ege])

print("* макс. балл = {}".format(max_mark))

print("* всего ВУЗов, в которые я прохожу: {}\n".format(len([x for x in iau if iau[x] <= sum_mark])))

