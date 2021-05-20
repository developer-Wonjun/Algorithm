N = int(input())
hansu = 0

for i in range(1,N+1):

    if i < 100:
        hansu +=1

    else:
        new_N = list(map(int,str(i)))

        if new_N[0] - new_N[1] == new_N[1] - new_N[2]:
            hansu +=1


print(hansu)