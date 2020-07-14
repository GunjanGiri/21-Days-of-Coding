a = str(input("Enter the encrypted message: "))
j = 0

for i in a:
    if i == " ":
        b = chr(ord(i))
        print(b ,end="")

    elif j % 2 == 0:
        b = chr(ord(i)-1)
        print(b , end="")
        j = j + 1

    elif j % 2 != 0:
        b = chr(ord(i)+1)
        print(b ,end="")
        j = j + 1

