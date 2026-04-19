
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
