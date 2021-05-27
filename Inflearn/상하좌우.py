n = int(input())
x,y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
command = ['L', 'R', 'U', 'D']


for plan in plans:

    for i in range(len(command)):

        if plan == command[i]:
            nx = x + dx[i]
            ny = y + dx[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        print('오류발생')
        continue

    x,y = nx,ny
print(x,y)