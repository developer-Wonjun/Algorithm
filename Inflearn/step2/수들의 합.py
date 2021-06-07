N,M = map(int,input().split())

a = list(map(int,input().split()))
sum = a[0]
c=0
lt = 0
rt = 1
while True:
    if sum < M:
        if rt <N:
            sum += a[rt]
            rt+=1
        else:
            break

    elif sum ==M:
        c+=1
        sum -=a[lt]
        lt +=1
    else:
        sum-=a[lt]
        lt+=1
print(c)