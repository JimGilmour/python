import os


for i in range(9):
    try:
        os.mkdir('dir_' + str(i + 1))
    except FileExistsError:
        pass

for i in range(9):
    try:
        os.rmdir('dir_' + str(i + 1))
    except FileNotFoundError:
        pass

print(list(i for i in os.listdir() if os.path.isdir(i)))

import sys

filename = sys.argv[0]
with open(filename, 'rb') as f:
    filename = os.path.basename(filename)
    name = filename.split('.py')[0] + '_copy'
    with open(name + '.py', 'wb') as f1:
        f1.write(f.read())