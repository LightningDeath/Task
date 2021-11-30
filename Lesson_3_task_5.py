from random import choice, randrange

first_words = ["автомобиль", "лес", "огонь", "город", "дом"]
second_words = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
another_words = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def jock(i, repeat=False):
    """
    Функция возвращает случайные шутки
    :param i: количество  шуток
    :param repeat: уникальность или нет шутки
    :return: возрат случайных шуток

    """

    jock_list = []
    fw, sw, aw = first_words.copy(), second_words.copy(), another_words.copy()
    list_of_min = min(fw, sw, aw)

    while i and len(list_of_min):
        number = randrange(len(list_of_min))
        if repeat:
            jock_list.append(f'{fw.pop(number)} {sw.pop(number)} {aw.pop(number)}')
        else:
            jock_list.append(f'{choice(first_words)} {choice(second_words)} {choice(another_words)}')
        i -= 1
    return jock_list


print(jock(5))
