N = int(input())
A = list(map(int,input().split()))
B = max(A)
C = []
for i in range(N):
    C.append(A[i]/B*100)

AVG = sum(C)/len(C)

print(AVG)