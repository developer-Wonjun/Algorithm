N,K = map(int,input().split())

a = []

for i in range(1,N+1):
    b = N%i

    if b == 0:
        a.append(i)
    

a.sort

if len(a) < K:
    print(-1)
else:
    print(a[K-1])

