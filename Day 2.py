m = int(input("Enter a Number: "))
for i in range(65, 70):
    m = m - 1
    for j in range(m+1 , 1, -1):
        print(" ", end="")
    for k in range(65, i, 1):
        print(chr(k), end="")
    for n in range(i, 64, -1):
        print(chr(n), end="")
    print("")
