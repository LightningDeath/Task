# Вычислить сумму тех чисел из этого списка, сумма цифр которых
# делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать
# в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить
# сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

result = []
i = 1
C = 0
summ = 0
second_summ = 0
# цикл для поиска четных чисел
while i <= 1000:
    if i % 2 == 0:
        n = i ** 3
        new_number = n
        result_number = 0
        A = 0
        # сразу считаем сумму чисел в числе:)
        while A != len(str(n)):
            last_number = new_number % 10
            new_number = new_number // 10
            result_number += last_number
            A += 1
        # и здесь же проверяем на соответствие условию задачи
        if (result_number % 7) == 0:
            result.append(result_number)
            summ += result_number
    i += 1
print('Сумма возведенных в куб четных чисел от 1 до 1000 и делящихся целочисленно на 7 равна: ', summ)
# производим проход по полученному списку с добавлением 17 к каждому элементу
for B in result:
    n = B + 17
    new_number = n
    result_number = 0
    while C != len(str(n)):
        last_number = new_number % 10
        new_number = new_number // 10
        result_number += last_number
        C += 1
    # проверка на соответствие условию задачи
    if (result_number % 7) == 0:
        second_summ += result_number
print('Сумма возведенных в куб четных чисел от 1 до 1000 с добавлением к ним 17'
      ' и делящихся целочисленно на 7 равна: ', second_summ)
