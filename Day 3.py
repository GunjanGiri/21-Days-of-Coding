import math

a = int(input("Enter the starting element of a series: "))
n = int(input("Enter the number of elements of the series: "))
r = int(input("Enter the common ratio: "))

for i in range(0, n):
    gp = a * math.pow(r, i)
    print(gp, end=" ")

Addition = (a * (1 - math.pow(r, n))) / (1 - r)
print()
print(Addition)

