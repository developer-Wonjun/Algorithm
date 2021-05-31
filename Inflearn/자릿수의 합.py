N = int(input())
s = list(map(int,input().split()))

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum+=int(i)
    return sum
    
max = 0
answer = 0
for x in s:
    tot = digit_sum(x)

    if tot > max:
        max = tot
        answer = x

print(answer)