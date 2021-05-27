N,K = map(int,input().split())

c = 0

while N != 1:

    if N % K == 0:

        N = N // K
        c +=1
    
    else:
        N -= 1
        c += 1


print(c)