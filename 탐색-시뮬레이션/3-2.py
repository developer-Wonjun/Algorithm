n = list(input())
c = ''
for i in n:
    try:
        b = int(i)
        c +=i
    except:
        pass
c = int(c)
a = [0]*(c+1)

for i in range(2,c+1):
    for j in range(1,i+1):
        if i%j == 0:
            a[i] +=1
            
print(c)
print(a.count(2))