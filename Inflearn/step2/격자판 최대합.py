N = int(input())

a = [list(map(int,input().split()))for _ in range(N)]

max = 0

for i in range(N):
    sum1=0
    sum2=0
    for j in range(N):
        sum1 += a[i][j]
        sum2 += a[j][i]

    if sum1 > max:
        max = sum1
    if sum2 > max:
        max = sum2
sum1 = sum2 =0

for i in range(N):
    sum1 += a[i][i]
    sum2 += a[i][N-i-1]
if sum1 > max:
    max = sum1
if sum2 > max:
    max = sum2
print(max)

