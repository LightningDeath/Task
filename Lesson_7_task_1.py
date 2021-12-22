import os

bra_path = ('settings', 'mainapp', 'adminapp', 'authapp')
if not os.path.exists('my_project'):
    os.mkdir('my_project')
    os.chdir(os.path.abspath('my_project'))
    for i in bra_path:
        if not os.path.exists(i):
            os.mkdir(i)
        else:
            print('Папка ', i, ' существует!')
else:
    print('Папка my_project существует!')
exit(3)
