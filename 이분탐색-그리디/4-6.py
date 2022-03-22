L = int(input())
arr = list(map(int,input().split()))
M = int(input())
res =0

arr.sort()
print(arr)
for i in range(M):
    arr[L-1] -=1
    arr[0] +=1

    arr.sort()
    print(arr)
print(arr)
print(arr[L-1]-arr[0])
