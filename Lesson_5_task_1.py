def rand_number(number):
    for number in range(1, number + 1, 2):
        yield number


for n in rand_number(30):
    print(n)
