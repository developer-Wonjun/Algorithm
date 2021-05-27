S = str(input())

s = list(S)
if '0' in s:
    s.remove('0')
c = s[0]
for i in s[1:]:

    if i == 1:
        c +=1
        print(c)
    else:
        c = c * int(i)
        print(c)


print(c)
