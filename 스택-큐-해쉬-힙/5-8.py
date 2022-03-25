import heapq as hq

a = [] 
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0 :
        if len(a) == 0:
            print(-1)
        else:
            print(abs(hq.heappop(a)))
    else:
        hq.heappush(a,-n)
        print(a)

# a =0
# b=[]

# while a != -1:

#     a = int(input())

#     if a == 0:

#         print(min(b))
#         b.clear()
#     elif a == -1:
#         break

#     else:

#         b.append(a)
