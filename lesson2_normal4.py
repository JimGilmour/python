a = [1, 5, 7, 3, 5, 2, 1, 5, 6, 7]

print(a)

b = list()

for c in a:
    if a.count(c) == 1:
        b.append(c)

        print(b)

