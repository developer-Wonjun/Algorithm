p = 'CBA'
n = 3
a = [['C','B','D','A','G','E'],['F','G','C','D','A','B'],['C','T','S','B','D','E','A']]


# while True:
#    


for i in range(n):
    b = ['C','B','A']
    for j in range(len(a[i])):

        if a[i][0] == b[0]:
            b.pop(0)
        a[i].append(a[i].pop(0))
            
        if len(b) == 0:
            print('#{0} YES'.format(i+1))
            break
    else:
        print('#{0} NO'.format(i+1))
    


