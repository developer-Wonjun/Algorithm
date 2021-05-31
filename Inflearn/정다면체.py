N,M = map(int,input().split())

a = [0]*(N+M+1)
sum = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        sum = i + j

        a[sum] +=1

        sum = 0

for i in range(N+M+1):
    if a[i] == max(a):
        print(i , end=' ')