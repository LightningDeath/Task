def thesaurus(*args):

    dict_of_name = {}
    for i in sorted(args):
        lt = i[0]
        if lt in dict_of_name:
            dict_of_name[lt] += [i]
        else:
            dict_of_name[lt] = [i]

    return dict_of_name


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Саша", "Петя", "Лера"))
