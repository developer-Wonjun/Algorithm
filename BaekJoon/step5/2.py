a = []

for i in range(9):
    a.append(int(input()))

b = max(a)
c = a.index(b) + 1
print(b)
print(c)
