def football_team(team):

    print(f'{team} - чемпион!')
    print(f'{team} {len(team)*'-'} чемпион!')

    team = team.lower() 

    print(f'Длина наименования: {len(team)}\nБуква (п) в имени команды: {"п" in team}\nКол-во букв (а) в имени команды: {sum(1 for i in team if i == "а")}')

def country(country, capital):
    print(f'Государство - {country}, столица - {capital}')

def oop():
    word = "объектно-ориентированный"
    print(f'{word[5:]}, {word[9:16]}, {word[14:16]}, {word[4]}{word[0]}{word[5]}, {word[10]}{word[12:14]}{word[19]}')

def two_strings(st, subst):
    if subst.lower() in st.lower():
        print("Подстрока есть")
    else:
        print("Подстроки нет")

def index(string, letter):
    finded_letters = [x for x in range(len(string)) if string[x] == letter]
    try:
        print(f'Первое вхождение: {finded_letters[0]},\nПоследнее: {finded_letters[-1]}')
    except:
        print(f'Букв {letter} в строке {string} - нет!')

def find_letters(string):
    letters = [letter for letter in string if not letter.isspace()]

    top = {}

    for letter in letters:
        top[letter] = top.get(letter, 0)+1

    sort_letters = sorted(top.items(), key=lambda x: (-x[1], x[0]))
    
    top_of_three = sort_letters[:3]

    print(f'{", ".join(f'{symbol} - {count}' for symbol, count in top_of_three)}')


ch = 1

while ch != 0:

    ch = int(input("Выберите задание\n(0 - выход)\n> "))

    match ch:
        case 0:
            pass
        case 1:
            team = input("Введите имя команды\n> ")
            football_team(team) 
        case 2:
            _country = input("Введите имя государства: ")
            _capital = input("Введите название столицы: ")
            country(_country, _capital)
        case 3:
            oop()
        case 4:
            st = input("Введите строку: ")
            subst = input("Введите подстроку: ")
            two_strings(st, subst)
        case 5:
            string = input("Введите строку: ")
            letter = input("Введите букву: ")
            index(string, letter)
        case 6:
            string = input("Введите строку: ")
            find_letters(string)