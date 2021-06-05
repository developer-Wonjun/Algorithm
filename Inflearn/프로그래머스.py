# M = int(input())
# load = list(map(int,input().split()))
def solution(M,load):
    c = 0
    result = 0
    i = 0
    while a.max() != 0:
            for x in range(len(load)):
                c += load[x]
                a[x] = 0
                for y in range(1,len(a)+1)
                    if c+load[y] <= M:
                        c+=load[y]
                        load[y]= 0
                        if y == load[-1]:
                            c=0
                            result+=1
                                                
M = int(input())
load = list(map(int,input().split()))
load.sort(reverse=True)
solution(M,load)
