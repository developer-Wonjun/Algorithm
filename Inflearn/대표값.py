N = int(input())
b = 0
sum = 0
c = 0
for i in range(N):
    a = list(map(int,input().split()))
    
    for j in a:
        sum += j
    
    b = sum / N

    for z in range(1,len(a)):
        if abs(b - a[z]) < abs(b - a[z-1]):
            c = a[z]

    
    print(round(b,0),(a.index(c)+1))
       



