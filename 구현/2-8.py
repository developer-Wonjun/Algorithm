N = int(input())

result = 0

for i in range(N):
    won = 0
    a = [0] * 7
    n = list(map(int,input().split()))
    
    for j in n:
        a[j] += 1
        
    if max(a) == 1:
        won = max(n) * 100
        
    elif max(a) == 2: 
        won = 1000 + (a.index(2))*100
    
    else:
        won = 10000 + (a.index(3)) * 1000
        
    if won > result:
        result = won

print(result)
        
        
    
    
    