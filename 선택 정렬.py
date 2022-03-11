arr = [9, 6, 7, 3, 5]

# 모든 배열 내 반복
for i in range(len(arr)):
    # i 번째 위치부터 최솟값 탐색
    for j in range(i, len(arr)-1):
        if arr[j] < arr[j+1]:
            minimun = j
        else:
            minimun = j+1
    # i번째 데이터와 최솟값 스왑
    arr[i], arr[minimun] = arr[minimun], arr[i]
    print(arr)

# 선택 정렬 특징
# 제자리 정렬 알고리즘 중 하나
# 배열 내 최솟값을 찾아 첫번째 데이터와 스왑
# 그 다음 최솟값을 찾아 두번째 데이터와 스왑
# ... 반복
# 시간 복잡도는 O(n^2) 인듯?