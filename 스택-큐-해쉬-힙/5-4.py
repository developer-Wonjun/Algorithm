N, M = map(int,input().split())
a = [(key,value) for key,value in enumerate(list(map(int,input().split())))]

res =0
b = a[M]
print(b)
while True:

    l = a.pop(0)

    if any(i[1] > l[1] for i in a):
        a.append(l)

    else:
        res +=1
    
    if b not in a:
        break

print(res)