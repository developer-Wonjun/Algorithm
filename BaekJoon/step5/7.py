C = int(input())

for i in range(C):
    a = list(map(int,input().split()))
    b = sum(a[1:])/a[0]
    cnt = 0
    for j in a[1:]:
        if j > b :
            cnt += 1
    
    n = cnt/a[0]*100
    print(f'{n:.3f}%')