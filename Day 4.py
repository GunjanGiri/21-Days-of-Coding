a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))
print("The prime numbers in the interval are: ", end=" ")

def prime():
    for i in range(a, b+1):
        if i > 1:
            for j in range(2, i):
                if(i % j) == 0:
                    break
            else:
                print(i, end=" ")

prime()