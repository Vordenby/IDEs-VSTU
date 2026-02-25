def first_task():
    a = []
    b = []
    
    a.append(4.5)
    a.append(3.4)
    a.extend([8.7, 1.3])

    b.append(14.5)
    b.append(3.4)
    b.extend([8.7, 11.3])

    a.insert(2, 100)
    a.insert(3, 100)

    b.insert(0, 200)
    b.insert(2, 200)

    print("Исходные списки:")
    print("1-й: ", a)
    print("2-й: ", b)

    del(a[0])
    del(b[0])

    a.remove(100)
    b.remove(200)

    print("\nПосле удалений:")
    print("1-й: ", a)
    print("2-й: ", b)

    sa = set(a)
    sb = set(b)
    sa_and_sb = sa & sb

    print("\nУникальные элементы:")
    print("1-й: ", sa)
    print("2-й: ", sb)
    print("Общие: ", sa_and_sb)

    c = a + b

    c_asc = sorted(c, reverse=False)
    c_desc = sorted(c, reverse=True)

    import statistics 

    sr_ar = statistics.mean(c[1::2])
    sr_geom = statistics.geometric_mean(c[0::2])

    c_max = max(c)
    c_min = min(c)

    print("\nИтоговые: ")
    print("3-й: ", c)
    print("Среднее арифметическое: ", sr_ar)
    print("Среднее геометрическое: ", sr_geom)
    print("Сортировка по возрастанию: ", c_asc)
    print("Сортировка по убыванию: ", c_desc)
    print(f'Максимум: {c_max}, Минимум: {c_min}')

def second_task(lst):
    
    mx_str = max([len(x) for x in lst])
    
    for i in lst:
        d = len(i)
        while d < mx_str:
            i += '_'
            d +=1
    print("Итоговый список строк: ", lst)


first_task()
print("\nДля задания 2 введите произвольное количество строк. Для окончания ввода - введите 0")
n = ''
lst = []
while n != '0':
    n = input()
    lst.append(n)
lst.remove('0')
second_task(lst)