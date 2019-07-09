a = [1, -5, 9, -2, 8, 2, -4]

b = []

for c in a:
    if c >= 0:
        d = c ** 0.5

    if d == int(d):
        b.append(int(d))

        print(b)


