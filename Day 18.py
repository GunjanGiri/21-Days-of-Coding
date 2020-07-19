n = int(input("Enter the number of test cases: "))

def divisible(a ,b ,n):

    for i in range(n):
        q = int(a / b)
        a1 = b * q

        if ((a * b) > 0):
            a2 = (b * (q + 1))
        else:
            a2 = (b * (q - 1))

        if (abs(a - a1) < abs(a - a2)):
            return abs(a - a1)
        else:
            return abs(a - a2)

for i in range(n):
    a , b = map(int,input("Enter two numbers: ").split())
    res = divisible(a, b, n)
    print("Number of steps: ",res)


