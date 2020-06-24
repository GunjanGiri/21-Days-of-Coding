a = int(input("Enter A Number: "))
s = 0

for i in range(1, a+1):
    if a % i == 0:
        if i % 2 != 0:
            s = s + i

print("Odd Factor Sum For The Number= ",s)