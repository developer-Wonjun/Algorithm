T = input()
a = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS',
    'TUV', 'WXYZ']
c = 0
for i in range(len(T)):
    for j in a:
        if T[i] in j:
            c += a.index(j)+3

print(c)

