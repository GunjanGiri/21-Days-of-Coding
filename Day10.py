a = list(input("Enter a list of integers: "))

b = [i for i in a if i != " "]

d = []

c = b[0]
b[0] = b[-1]
b[-1] = c

d.append(b)

print("List with first and last letter swapped: ",d)