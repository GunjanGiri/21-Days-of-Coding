a = int(input("Enter a number: "))

b = 1
c = 2

while c <= a/c:
    if a % c == 0:
        b = c
        a = a/c
    else:
        c = c + 1

if b < a:
    b = a

print("Largest Prime Factor Of The Number= ",b)