def quick_sort(arr):
    # 입력된 배열의 길이가 1보다 클 경우
    if len(arr)>1:
        # pivot은 항상 수열의 오른쪽 끝 값
        pivot = arr[-1]

        # 왼쪽 포인터는 왼쪽 첫번째 값
        left = 0

        # 오른쪽 포인터는 왼쪽에서 오른쪽으로 한칸씩 이동
        for right in range(len(arr)):

            # 오른쪽 포인터의 값이 pivot보다 작을 경우, 스왑
            if arr[right] < pivot:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                print(arr)

        # 반복문을 통해 오른쪽 포인터가 pivot에 닿았으므로,
        # pivot과 왼쪽 포인터의 값 스왑
        arr[-1], arr[left] = arr[left], arr[-1]
        print(arr)

        # 이동한 pivot의 위치를 기준으로 왼쪽 배열과 오른쪽 배열로 나눠 재귀 적용
        left_side = quick_sort(arr[:left])
        right_side = quick_sort(arr[left+1:])

        # 받아온 정렬된 데이터들을 통합
        return left_side + [arr[left]] + right_side

    # 길이가 1 이하일 경우 그대로 return
    else:
        return arr

arr = [5, 3, 7, 6, 2, 1, 4]
start, end = 0, len(arr)-1
print(quick_sort(arr))

# 퀵 정렬 특징
# 평균 O(nlogn)의 시간 복잡도
# 평균적인 상황에서 최고의 성능
# 하지만 구현하기에 복잡함