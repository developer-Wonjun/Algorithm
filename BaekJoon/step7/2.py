N = int(input())
s = list(map(str,input()))
r = 0
for i in range(N):
    r += int(s[i])

print(r)