N = int(input())
a = [0] * (N+1)

s=0
for i in range(2,N+1):
    if a[i] == 0:
        s += 1

        for j in range(i,N+1,i):
            a[j] = 1

print(s)
