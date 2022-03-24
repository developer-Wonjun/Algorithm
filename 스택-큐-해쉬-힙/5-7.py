a = list(map(str,input()))
ad = {i:0 for i in a}
b = list(map(str,input()))
bd = {i:0 for i in a}
res = 0

for i in a:
    ad[i] +=1
for i in b:
    bd[i]+=1

for key,value in ad.items():
    
    aa = bd[key]

    if aa == value:
        res +=1

if res == len(ad):
    print('YES')
else:
    print(res)
    print('NO')

print(len(ad))