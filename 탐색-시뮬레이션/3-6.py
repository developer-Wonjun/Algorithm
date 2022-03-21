N = int(input())
a = [list(map(int,input().split())) for _ in range(N)]
largest = 0
da1=da2=0
for i in range(N):
    ga=se=0
    da1 += a[i][i] #대각 합
    da2 += a[i][N-i-1] # 대각 합
    for j in range(N):
        ga += a[i][j] #행 더하기
        se += a[j][i] #열 더하기
    
    if ga > largest:
        largest = ga
    elif se > largest:
        largest = se
if da1 > largest:
    largest = da1
if da2 > largest:
    largest = da2

print(largest)