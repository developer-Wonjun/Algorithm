N = int(input())
n = list(map(int,input().split()))
M = int(input())
m = list(map(int,input().split()))


a = n+m

a.sort()
print(a)