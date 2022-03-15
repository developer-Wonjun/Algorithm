N = int(input())

result = [0]*(N+1)
for i in range(2,N+1):

    for j in range(1,i+1):
        if i%j == 0:
            result[i] += 1
a = []        
for i in range(len(result)):
    if result[i] == 2:
        a.append(i)
        
print(len(a))