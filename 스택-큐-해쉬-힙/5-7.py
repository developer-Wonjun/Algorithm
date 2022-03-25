a = input()
b = input()
da = dict()
db = dict()
res = 0
for i in a:
    da[i] = da.get(i,0) +1
for i in b:
    db[i] = db.get(i,0) +1
print(da)

for key,value in da.items():
    
    if key in db.keys():
        aa = db[key]
        if aa == value:
            res +=1
        else:
            print('NO')
            break
    else:
        print('NO')
        break
else:
    print('YES')