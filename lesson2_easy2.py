a = [3, 7, 4, 6, 6, 3, 5]
b = [5, 6, 8, 2, 6, 8, 5, 3, 6, 8, 4, 6]

for c in b:
    while c in a:
        a.remove(c)

        print(a)

