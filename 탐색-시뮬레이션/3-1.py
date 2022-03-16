N = int(input())

for i in range(N):
    n = input().lower()
    a = 0
    if len(n)%2 == 1:

        for j in range((len(n)-1)//2):
            if n[j] == n[-j-1]:
                pass
            else:
                print('#',i+1,' ','NO')
                a +=1
        if a == 0:
            print('#',i+1,' ','YES')
        else:
            print('#',i+1,' ','NO')
    else:
        
        for j in range((len(n))//2):
            
            if n[j] == n[-j-1]:
                pass
            else:
                a +=1
        if a == 0:
            print('#',i+1,' ','YES')
        else:
            print('#',i+1,' ','NO')