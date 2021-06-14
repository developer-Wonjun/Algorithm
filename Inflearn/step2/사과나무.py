N = int(input())

a = [list(map(int, input().split()))for _ in range(N)]

k = N//2  # 2
lk = k  # 2
rk = k + 1  # 3
apple = 0
for i in range(N):
    apple += sum(a[i][lk:rk])
    if i < k:
        lk -= 1
        rk += 1
    else:
        lk += 1
        rk -= 1
print(apple)
