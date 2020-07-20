import math

import random

a = int(input("Enter starting point of range: "))
b = int(input("Enter ending point of range: "))
c = int(input("Enter number of iterations: "))
n = 0

for i in range(1 , c+1):
    r = random.randint(a, b)

    x = math.sqrt(r)
    y = (x - math.floor(x))

    if y == 0:
        print(x ,end=",")
        n += 1


prob = n/c

print("\nProbability=",prob)