N = int(input())
a = [list(map(int,input().split())) for _ in range(N)]
result = 0
ap=bp=N//2 # 값이 유동적일 수 있음. 따라서 절대적인 값은 안됨.
for i in range(N):
    
    for j in range(ap,bp+1):
        result += a[i][j]
    if i <N//2:
        ap -=1
        bp +=1
    else:
        ap +=1
        bp -=1
print(result) 
        