dict_of_users = {}
list_of_hobby = []
with open('hobby.csv', encoding='utf-8') as hobby:
    for line in hobby:
        list_of_hobby.append(line.replace('\n', ''))
with open('users.csv', 'r', encoding='utf-8') as users:
    n = 0
    for line in users:
        if n <= len(list_of_hobby) - 1:
            dict_of_users[line.replace('\n', ' ').replace(',', ' ')] = list_of_hobby[n]
        else:
            dict_of_users[line.replace('\n', '').replace(',', ' ')] = None
        n += 1
if n == len(list_of_hobby):
    print('Code 1')
with open('user_data.csv', 'w', encoding='utf-8') as ud:
    ud.write(str(dict_of_users))
