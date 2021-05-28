N = int(input())

c = 0
for i in range(N+1):
    for j in range(60):
        for t in range(60):
            if '3' in str(i) + str(j) + str(t):
                c +=1

print(c)
