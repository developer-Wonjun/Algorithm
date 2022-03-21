N = int(input())
a = [list(map(int,input().split())) for _ in range(N)]
M = int(input())

for i in range(M):

    z,x,c = map(int,input().split())

    if x == 0:
        for j in range(c):

            a[z-1].append(a[z-1].pop(0))
    else:
        for j in range(c):

            a[z-1].insert(0,a[z-1].pop())

print(a)
lt=0
rt=4
result=0
for i in range(N):

    for j in range(lt,rt+1):
        result+=a[i][j]
        print(j)
    if i < N//2:
        lt +=1
        rt -=1
    else:
        lt -=1
        rt +=1
    print(lt,' ',rt)
print(result)