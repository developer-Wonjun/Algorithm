M,N = map(int,input().split())
a = list(map(int,input().split()))
#rt를 모두 수용할 수  있는건 무조건 답
lt = 1
rt = sum(a)
result=0
while lt <= rt:
    res = 0
    mid = (rt+lt)//2
    r = mid
    sum = 0
    for i in range(M):#23 22 20 17 13 8 2  16 8   9  3
        if sum+a[i] > mid: 
            res+=1
            sum=a[i]
        else:
            sum += a[i]
        if i == M-1:
            if a[i] <= r:
                res+=1
    
    if res <= N:
        result = mid
        rt = mid -1
    else:
        lt = mid +1

print(result)