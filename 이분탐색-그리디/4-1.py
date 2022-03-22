#이분검색 -> 결정알고리즘 상황에서 사용
# 결정알고리즘 특징 -> 찾고자하는 값이, 특정 범위에있다.
# 이따 값을 딱 정해놓고(중간값) 정답이 되냐, 안되냐 확인한다.
# 오답이면, 범위를 좁혀가며 정답을 찾아간다.
N, M = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
lt = 0
rt = N-1
while lt<=rt:
    mid = (lt+rt)//2
    
    if a[mid] == M:
        print(mid+1)
        break
    elif a[mid] >= M:
        rt = mid-1
    else:
        lt = mid +1
    
    