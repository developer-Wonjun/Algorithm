N = int(input())
check=N
A=0
c = 0
T = 0
while True:
    A = N//10 + N%10
    T = (N%10)*10 + (A%10)
    c +=1
    N = T
    if check == T:
        break

print(c)
