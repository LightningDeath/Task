# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида:
# 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их
# к корректному виду. Можно ли при этом не создавать новый список?

task_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for n in task_list:
    i = task_list.index(n)
    # разбиваем строку по пробелу и создаем встроенный лист
    task_list[i] = n.split(' ')
    # берем последнее слово в встроенном листе, которое обозначает имя
    name = task_list[i][-1]
    L = len(task_list[i])
    profession = ''
    # проходим по встроенному списку минус последнее слово для получения профессии
    for a in range(0, L-1):
        profession = profession + ' ' + task_list[i][a]
    message = f'Приветствую, уважаемый(ая) {name.title()}! Вы самый лучший{profession}!'
    print(message)