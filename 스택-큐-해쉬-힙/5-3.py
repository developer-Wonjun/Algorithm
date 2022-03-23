from re import L


N,K=map(int,input().split())

a = [x for x in range(1,N+1)]

last = 0
q = []
while len(a) != 1:

    a.append(a.pop(0))
    last +=1

    if last ==3:
        a.pop()
        last =0

print(a[0])
