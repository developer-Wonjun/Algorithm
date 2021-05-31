N = int(input())

for i in range(1,N+1):
    t = ''
    z = ''
    a = list(input().upper())
    for j in a[::-1]:
        t +=j
    for n in a:
        z +=n
    
    if t == z:
        print('#%d YES' %(i))
    else:
        print('#%d NO' %(i))

    
    
    