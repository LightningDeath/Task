# добавление суммы продажи

from sys import argv

with open('bakary.csv', 'a', encoding='utf-8') as add:
    with open('bakary.csv', 'r', encoding='utf-8') as read:
        if len(argv) > 1 and [n for n in argv[1:] if "." in n and n.replace('.', '').isdigit()]:
            if round(float(argv[1]), 3) <= 99999.999:
                print(f'{round(float(argv[1]), 3):>010}', file=add)
            else:
                print('Число должно быть меньше 99 999,999')
        else:
            print(read.read())
