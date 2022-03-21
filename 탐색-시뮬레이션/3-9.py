N = int(input())
a = [list(map(int,input().split())) for _ in range(N)]
a.insert(0,[0]*(N+2))
a.append([0]*(N+2))

for i in range(N):
    
    a[i+1].insert(0,0)
    a[i+1].append(0)
result = 0
for i in range(1,N+1):

    for j in range(1,N+1):

        # 이렇게 하는건 너무 비효율
        # dx=[-1,0,1,0]
        # dy=[0,1,0,-1]
        # 선언해서 if all() for i in range(4): 돌리자
        if (a[i][j] > a[i-1][j]) and (a[i][j] > a[i+1][j]) and (a[i][j]>a[i][j+1]) and (a[i][j]>a[i][j-1]):
            result+=1

print(result)

    