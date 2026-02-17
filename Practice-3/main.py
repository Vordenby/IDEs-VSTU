def football_team(team):

    print(f'{team} - чемпион!')
    print(f'{team} {len(team)*'-'} чемпион!')

    team = team.lower() 

    print(f'Длина наименования: {len(team)}\nБуква (п) в имени команды: {"п" in team}\nКол-во букв (а) в имени команды: {sum(1 for i in team if i == "а")}')

def country(country, capital):
    print(f'Государство - {country}, столица - {capital}')

def oop():
    word = "объектно-ориентированный"
    