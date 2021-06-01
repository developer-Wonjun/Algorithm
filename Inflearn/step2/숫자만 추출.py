N = input()
s=''
c = 0
for i in N:
    if i.isdigit():
        s+=str(i)

t = int(s)
for i in range(1,t+1):
    if t%i==0:
        c+=1


print('%d\n%d'%(t,c))