import cmath

a = float(input("Enter a : "))
b = float(input("Enter b : "))
c = float(input("Enter c : "))

d = b*b - 4*a*c

e = (-b + cmath.sqrt(d))/(2*a)

f = (-b - cmath.sqrt(d))/(2*a)

print('The Discriminate is ',d)

print('The Roots of the Equations are ',e,f)
