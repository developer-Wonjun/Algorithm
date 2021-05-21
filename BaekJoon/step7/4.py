T = int(input())
for a in range(T):
    R,array = input().split()
    t = ''

    for i in array:
        t += int(R)*i
    print(t)


