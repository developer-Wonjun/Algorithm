#최솟값 구하기
N = int(input())
n = list(map(int,input().split()))

avr = round(sum(n)/len(n))
cnt = 100
s = 0 #굳이 이걸 안하고, enumerate로 표시할수있었음......
for i in range(N):
    
    if cnt > abs(n[i] - avr):
        cnt = abs(n[i] - avr)
        s = i+1
    elif cnt == abs(n[i] - avr):
        if n[s-1] < n[i]:
            cnt = abs(n[i] - avr)
            s = i+1
        
print(avr, s)
            
        