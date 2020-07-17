a = int(input("First element of the series: "))
b = int(input("Second element of the series: "))
c = int(input("Number of elements of the series: "))


def fibo(c):
    if c <= a:
        return a
    elif c == b:
        return b
    else:
        s = fibo(c-1) + fibo(c-2)
        return s

print("Fibonacci Series:",end=" ")
for i in range(1 , c+1):
    print(fibo(i) ,end=",")