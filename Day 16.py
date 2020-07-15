a = str(input("Enter the string :"))

def character(a):
    b = 256
    c = [0] * b
    for i in range(len(a)):
        c[ord(a[i])] += 1

    d = 0
    e = 0

    for i in range(b):
        if c[i] > c[d]:
            e = d
            d = i
        elif (c[i] > c[e]) and (c[i] != c[d]):
            sm = i

    print("The character which appears the most: ", chr(d))
    print("After replacing: ", a.replace(chr(d), chr(e)))


character(a)