from itertools import islice, zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

res = (n for n in zip_longest(tutors, klasses) if len(tutors) > len(klasses))

print(type(res))
print(*islice(res, 10))
print(list(islice(res, 3)))
