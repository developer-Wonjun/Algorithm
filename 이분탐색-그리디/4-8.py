N = int(input())
a = list(map(int,input().split()))
res =0
s = ''
c = 0
lt = 0
rt = N-1

while lt<=rt:
    L = a[lt]
    R = a[rt]
    
    if L < c and R < c:
        break
    elif L > c and R > c:
        m = min(L,R)
    else:
        m = max(L,R)
    res+=1
    c=m
    if a.index(m)==lt:
        s+='L'
        lt+=1
    else:
        s+='R'
        rt-=1   
         
print(res)
print(s)


