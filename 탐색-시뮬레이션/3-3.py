arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in range(10):
    
    a,b=map(int,input().split())
    if a == b :
        pass
    elif (b - a) %2 == 1: # 5~10   갯수 짝수
        
        for j in range(int(((b-a)/2)+0.5)): 
            q = arr[a-1] #a 5  b 10 가정
            w = arr[b-1]
            arr[a-1] = w
            arr[b-1] = q
            a+=1
            b-=1
    else:
        for j in range(int((b-a)/2)): 
            q = arr[a-1] #a 5  b 10 가정
            w = arr[b-1]
            arr[a-1] = w
            arr[b-1] = q
            a+=1
            b-=1

print(arr)
        