s = list(map(str,input()))
a = list('abcdefghijklmnopqrstuvwxyz')
b = [-1]*26

for i in range(len(s)):
    p = a.index(s[i])

    if b[p] == -1:
        b[p] = i

for j in b:
    print(j, end=" ")