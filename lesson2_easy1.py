
a = ['яблоко','банан', 'киви', 'арбуз']

b = len(max(a, key=len))

for index, item in enumerate(a, start=1):

    print("{}. {}".format(index, item.rjust(b)))

    