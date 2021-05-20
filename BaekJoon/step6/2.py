def d(A):
    A = A + sum(map(int,str(A)))
    return(A)

a =[0]*10001

for i in range(1,10001):
    a[i] = d(i)

    if i not in a:
        print(i)