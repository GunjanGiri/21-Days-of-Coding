def frequency_calculator(x):
    f = dict()
    while (x):
        a = x % 10
        if (a in f):
            f[a] = (f[a] + 1)
        else:
            f[a] = 1
        x = int(x / 10)
    print(f)


x = int(input("enter the number: "))
frequency_calculator(x)
