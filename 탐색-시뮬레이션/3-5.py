N,M = map(int,input().split())
A = list(map(int,input().split()))

result = 0
for i in range(N):
    a = 0
    for j in range(i,N):
        a +=A[i]
        print(a,'##########')
        if a == M:
            result +=1
            break
        elif a >M:
            break
print(result)
