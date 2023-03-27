x = input("Sisesta number\n")
if int(x) < 0:
    x = '' + x[1:]
    print('-' + x[::-1])
else:
    print(x[::-1])