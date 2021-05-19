a = int(input())

for i in range(a):
    b = input()
    c = list(b)
    sum = 0
    d =1

    for j in c:
        if j == 'O':
            sum += d
            d += 1
        else:
            d = 1

    print(sum)