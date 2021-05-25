n,k = map(int,input().split())

a = list(map(int,input().split()))
b = set(a)
a = list(b)
a.sort(reverse=True)

print(a[k-1])
