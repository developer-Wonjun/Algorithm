M,N = map(int,input().split())
a = list(map(int,input().split()))

lt = 0
rt = len(a)

while lt <= rt:
    
    mid = (lt+rt)//2
    
    for i in range(lt,rt-1):
        pass