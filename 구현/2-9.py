N = int(input())


n = list(map(int,input().split()))

result = 0
gasan = 0

for i in n:
    
    if i == 0:     
        gasan = 0
    
    else:  
        gasan +=1
        result += gasan
        
print(result)