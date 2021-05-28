n = input()

row = int(n[1])
column = int(ord(n[0])) - int(ord('a')) + 1

steps = [(-2,-1), (-2,1),(2,-1),(2,1),(-1,2),(1,2),(-1,-2),(1,-2)]
c=0

for step in steps:
    next_r = row + step[1]
    next_c = column + step[0]

    if next_r >=1 and next_r <= 8 and next_c >=1 and next_c <=8:
        c +=1

print(c)