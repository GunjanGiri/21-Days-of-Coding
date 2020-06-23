n = int(input('enter the size of list:'))
a = list(map(int, input('Enter entries with space:').split()))

a.sort()
k = a[0]
for i in a:
    if i > k:
        k = i
for l in range(a.count(k)):
    a.remove(k)
print(a[-1])