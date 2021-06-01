
t=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
mid=0
for i in range(1,11):
    A,B=map(int,input().split())
    a = A-1
    b = B-1
    if (B-A) == 1:
        c = 1
    elif (B-A)%2 ==1:
        c = (B-A)//2 +1
    else:
        c = (B-A)//2
    for j in range(c):
        t[a], t[b] = t[b], t[a]
        a+=1
        b-=1

for i in t:
    print(i,end=' ')


