import os
from collections import defaultdict
from os.path import dirname

a = input('Working here or another dir? \n(1 - here; 2 - another)\n')
if a == '2':
    os.chdir(input('Enter path: '))
elif a == '1':
    os.chdir(dirname(__file__))
else:
    print('Wrong option selected! \nWork will continue in the current directory.\n')
root_dir = os.getcwd()
size_files = defaultdict(int)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        size_of_file = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
        size_files[size_of_file] += 1
for size_files, nums in sorted(size_files.items()):
    print(f'{size_of_file}:{nums}')
exit(3)
