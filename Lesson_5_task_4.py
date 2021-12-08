src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

biggest = [num for idx, num in enumerate(src) if src[idx - 1] < src[idx] and idx > 0]

print(biggest)
