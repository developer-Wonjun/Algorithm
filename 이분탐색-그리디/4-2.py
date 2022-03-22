#이분검색 -> 결정알고리즘 상황에서 사용
# 결정알고리즘 특징 -> 찾고자하는 값이, 특정 범위에있다.
# 이따 값을 딱 정해놓고(중간값) 정답이 되냐, 안되냐 확인한다.
# 오답이면, 범위를 좁혀가며 정답을 찾아간다.

K, N = map(int,input().split())
a = list(map(int,input().split()))

#답은 1 ~ 802(가장 긴 것)
lt = 1
rt = max(a)
re = 0
while lt <=rt:
    c =0
    mid =(rt+lt)//2
    for i in range(K):
        c += a[i]//mid
    
    if c >= N:
        re = mid
        lt = mid +1
    else:
        rt = mid -1
print(re)