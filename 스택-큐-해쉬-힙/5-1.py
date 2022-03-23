n,m = map(int,input().split())

n = list(map(int,str(n)))
# stack - LIFO  append / pop()
# queue - FIFP  insert(0) / pop(0)
c = 0
stack = []

for i in n:

    while stack and m>0 and i>stack[-1]:
        stack.pop()
        m -= 1
    stack.append(i)

if m != 0 :
    stack = stack[:-m]

print(stack)


