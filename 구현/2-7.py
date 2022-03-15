from ast import While


N = int(input())
n = list(map(int,input().split()))

a = []

def reverse(x):
    
    # res = 0
    # while x>0:    
    #     t = x%10
    #     res = res*10 + t
    #     x = x//10            이 코드가 자릿수 바꾸는 정석 나는 노가다로 했음....
    
    if x>= 1000:
        a = x//1000 + (((x%1000)//100)*10) + ((((x%1000)%100)//10)*100) + ((((x%1000)%100)%10)*1000)
    
    elif x >= 100:
        a = x//100 + (((x%100)//10)*10) + (((x%100)%10)*100)
    elif x >= 10:
        a = x//10 + ((x%10)*10)
    else:
        a = x
    return a

def isPrime(x):
    if x == 1:
        return 0
    cc = 0
    for i in range(1,x+1):
        if x%i == 0:
            cc+=1
    return cc
        

for i in n:
    a.append(reverse(i))

for i in range(len(a)):
    aa = isPrime(a[i])
    if aa == 2:
        print(a[i],end=' ')


    
    