a = [1, 56, 342, 7, 6, 3, 78, 54, 7, 8, 12, 34, 6]

print(a)

b = []

for c in a:
    if c % 2 == 0:
        b.append(c / 4)

    else:
        b.append(c * 2)

        print(b)

        