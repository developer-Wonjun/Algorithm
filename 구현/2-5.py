N,M = map(int,input().split())
#원소가 여러개 있는 리스트 초기화 하는 방법 lst=[0]*(개수)
arr = [0] *(N+M+1)

for i in range(1,N+1):
    for j in range(1,M+1):
        arr[i+j] +=1

result = []
for i in range(len(arr)):
    if arr[i] == max(arr):
        result.append(i)
        
for i in result:
    print(i,end=' ')
