a = int(input("Enter a binary number:"))
b = " "
c = 0
i = 0

while a != 0:
    d = a % 10
    c = c + d*pow(2, i)
    i = i + 1
    a = int(a/10)

b = b + chr(c)
print("Character: ", b)
