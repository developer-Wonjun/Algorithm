T = int(input())
b = []
for i in range(T):
    n,s,e,k = map(int,input().split())

    a = list(map(int,input().split()))

    for j in range(s-1,e):

        b.append(a[j])

    b.sort()
    print('#',T,':',b[k-1])


