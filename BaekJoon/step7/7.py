A,B = map(str, input().split())
a = list(A)
b = list(B)

a = a[2] + a[1] + a[0]
b = b[2] + b[1] + b[0]


if a > b:
    print(a)
else:
    print(b)