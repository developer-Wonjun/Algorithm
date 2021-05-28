S = input()
s = list(S)
a = []
c=0
t=''
for i in range(len(s)):
    if s[i].isalpha():
        a.append(s[i])

        s[i] = 0
a.sort()
for i in range(len(s)):
    c += int(s[i])
    print(c)
for i in a:
    t += str(i)

print(t+str(c))

