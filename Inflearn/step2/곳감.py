N = int(input())
a = [list(map(int, input().split()))for _ in range(N)]

M = int(input())

for i in range(M):
    h, t, k = map(int,input().split())
    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())
k = N//2
lk = 0
rk = N
gam = 0
for i in range(N):
    gam += sum(a[i][lk:rk])
    if i < k:
        lk +=1
        rk -=1
    else:
        lk -=1
        rk +=1
print(gam)
