N = int(input())
max = 0
n = []
for i in range(N):
    t = input().split()
    t.sort()

    a,b,c = map(int,t)

    if a==b and b==c:
        max = 10000+ (a*1000)
    elif (a==b and b !=c):
        max = 1000+(a*100)
    elif (a !=b and b==c):
        max = 1000+(b*100)
    else:
        max = c*100
    n.append(max)

n.sort()

print(n[N-1])