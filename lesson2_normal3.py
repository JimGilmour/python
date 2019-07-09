

import random

rand_list = []
elem_count = int(input('введите количество элементов'))

for a in range(elem_count):
    rand_list.append(random.randint(-999, 999))

    print(rand_list)