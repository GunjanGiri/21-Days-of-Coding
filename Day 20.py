l = int(input("Length of the array: "))
a = list(map(int,input("Enter the array: ").split()[:l]))
x = int(input("The condition or sum: "))
c = 0

for i in range(0,l):
    if a[i] <= x:
        c = c + 1

    for j in range(i+1,l):
        if a[i] + a[j] <= x:
            c = c + 1

        for k in range(j+1,l):
            if a[i]+ a[j]+a[k] <= x:
                c = c + 1


if c == 0:
    print("Number of such possible combinations= -1")

else:
    print("Number of such possible combinations= ",c)