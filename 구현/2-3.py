N,K = map(int,input().split())
#N개의 자연수... 합의 수중 K번째로 큰거
n = list(map(int,input().split()))
res = set() #합의 중복이 있을수도잇으니 중복제거해주는 set

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
           res.add(n[i]+n[j]+n[k]) #set 은 add로 추가.
           
res = list(res)
res.sort(reverse=True)

print(res[K-1]) 

