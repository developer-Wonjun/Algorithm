T = list(input().lower())
t = list(set(T))

c = []

for i in t:
    
    count = T.count(i)
    c.append(count)

if c.count(max(c)) >= 2:
    print('?')

else:
    print(t[c.index(max(c))].upper())