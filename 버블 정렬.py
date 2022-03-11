arr = [5, 2, 9, 1, 6]
length = len(arr)
print(f"정렬 전: {arr}")

# 배열의 크기만큼 반복
for i in range(length):
    # 배열의 총 크기에서, i값과 1을 뺀 만큼 반복한다.
    for j in range(0, length-i-1):
        # 현재 j위치의 값이 j+1 위치의 값보다 크다면
        if arr[j]>arr[j+1]:
            # 두 값의 위치를 변경한다.
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(f"정렬 후: {arr}")

# 버블 정렬 특징
# 구현하기 쉽지만 모든 인접한 값을 비교해야 한다.
# 따라서 시간복잡도는 항상 O(n^2)