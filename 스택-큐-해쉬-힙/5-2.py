a = '(((()(()()))(())()))(()())'

a = list(a)

box = []
res = 0

for i in range(len(a)):

    if a[i] == '(' and a[i+1] == ')':
        res += len(box)
    
    elif a[i] =='(' and a[i+1] == '(':
        box.append('box')

    elif a[i] ==')' and a[i-1] == ')':
        box.pop()
        res+=1

print(res)
