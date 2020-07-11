a = int(input("Enter a long integer: "))
b = str(a)
n = len(str(a))
e = 0
o = 0

for i in range(0,n):
    if i % 2 == 0:
        e = e + int(b[i])
    elif i % 2 != 0:
        o = o + int(b[i])

d = o - e

if d == 0:
    print("YES")
else:
    print("NO")