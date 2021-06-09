aa= []
for i in range(0, 10):
    aa.append(i)


for i in range(0, 10):
    aa[i] = int(input(str(i +1) + "번째 숫자 :"))


hap = 0

for i in aa:
   hap+=i

print("합계 ==>",hap)
