N = int(input())
a = dict()
for i in range(N):
    a[input()]=0
for j in range(N-1):
    a[input()]+=1

#dict = dick의 key값을 리스트의 인덱스로 생각하자
a = dict(map(reversed,a.items()))
print('@@@@',a[0])