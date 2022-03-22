#그리디 = 정렬
n = int(input())
arr = []
for i in range(n):
    a ,b = map(int,input().split())

    arr.append((a,b))

arr.sort(key=lambda x: (x[1],x[0]))
print(arr)


res =0
et =0
for s,e in arr:
    if s >= et:
        res +=1
        et =e


print(res)
