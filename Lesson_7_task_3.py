import os
import shutil
from collections import defaultdict
from os.path import relpath

os.chdir('my_project')
root_dir = os.getcwd()
project_files = defaultdict(list)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        rel_path = relpath(os.path.join(root, file), root_dir)
        project_files[ext].append(rel_path)
r = project_files.get('html')
if not os.path.exists('templates'):
    os.mkdir('templates')
    for i in r:
        a = os.path.dirname(i).split('\\')[-1]
        if not os.path.exists(os.path.join('templates', os.path.dirname(i).split('\\')[-1])):
            os.mkdir(os.path.join('templates', a))
            shutil.copy2(i, os.path.join('templates', os.path.dirname(i).split('\\')[-1],
                                         os.path.basename(i)))
        else:
            shutil.copy2(i, os.path.join('templates', os.path.dirname(i).split('\\')[-1],
                                         os.path.basename(i)))
else:
    print('Папка templates уже сущесвует!')
exit(4)
