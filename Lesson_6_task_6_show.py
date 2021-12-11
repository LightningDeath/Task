# показ значений

from sys import argv

with open('bakary.csv', 'r', encoding='utf-8') as show:
    if 1 < len(argv) < 4 and [n for n in argv[1:] if n.isdigit()]:
        if len(argv) == 3:
            start, finish = map(int, argv[1:])
            print(*(a for n, a in enumerate(show) if start - 1 <= finish), sep='')
        else:
            print(*(a for n, a in enumerate(show) if n >= int(argv[1])-1), sep='')
    else:
        print(show.read())