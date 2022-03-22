N = int(input())
arr = []
for i in range(N):
    z,x = map(int,input().split())
    arr.append((z,x))

res = 0
cnt = 0
for a in range(N):
    cnt = 0
    for b in range(N):
        if a != b:
            if (arr[a][0] > arr[b][0]) or (arr[a][1] > arr[b][1]):
                cnt +=1
    if cnt == (len(arr)-1):
        res +=1

print(res)
    
