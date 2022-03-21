
r = 0
l = 0
re = set()
def check(a):
    for i in range(9):
        c1 = [0]*10
        c2 = [0]*10
        for j in range(9):
            c1[a[i][j]] =1
            c2[a[j][i]] =1
        if sum(c1) !=9 or sum(c2) !=9:
            return False
    for q in range(3): # 3*3 배열 이부분을 못풀었음. 필기하면서하자.
        for w in range(3): #애초에 for 문 2개를 돌아야 3*3을 특정해주는 상태가 되어버림
            c3 = [0]*10 
            for e in range(3):
                for r in range(3):
                    c3[a[q*3+e][w*3+r]] =1
            if sum(c3) != 9:
                return False
        
    return True

a = [list(map(int,input().split())) for _ in range(9)]

if check(a):
    print('YES')
else:
    print('NO')
    