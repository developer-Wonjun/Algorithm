N = int(input())
n = list(map(int,input().split()))
M = int(input())
m = list(map(int,input().split()))
a = 0
b = 0

t =[]
while a<N and b<M:
    if n[a] <= m[b]:
        t.append(n[a])
        a+=1
    else:
        t.append(m[b])
        b+=1
if a<N:
    t=t+n[a:]
if b<M:
    t=t+m[b:]
for z in t:
    print(z,end=' ')