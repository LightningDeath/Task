translate_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два',
                  'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                  'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def tr_f(user_word):
    if user_word.istitle():
        u_word = user_word.lower()
        return translate_dict.get(u_word).title()
    return translate_dict.get(user_word)


print(tr_f(input('Введите число от 0 до 10 на английском для перевода: ')))
