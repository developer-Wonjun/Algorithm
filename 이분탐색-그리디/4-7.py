N,M = map(int,input().split())
a = list(map(int,input().split()))

a.sort()
res=0
weight=0
for i in a:
    if weight+i <=M:
        weight+=i
    else:
        res+=1
        weight=i
print(res)