src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

dict = {n: 0 for n in src}

for n in src:
    dict[n] += 1
print([n for n in dict if dict[n] ==1])
