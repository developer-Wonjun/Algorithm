T = int(input())

c = []

for a in range(T):
    N,s,e,k = map(int,input().split())
    n = list(map(int, input().split()))

    m = []
    
    n = n[s-1:e] #알아두기.  
        
    m.sort()
    c.append(m[k-1])
    
for i in range(len(c)):
    
    print('#',i+1,' ',c[i])   
    
    
    