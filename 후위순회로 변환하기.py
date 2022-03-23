pre_order = [7,3,1,5,4,12,10,8]
in_order = [1,3,12,4,5,7,8,10]

def change_to_post(pre_arr, in_arr):
    if len(pre_arr) == 0:
        return
    # 전위 순회 리스트의 첫번째 요소가 현재 층의 루트
    root = pre_arr[0]
    # 루트 요소를 기준으로 나누어 다음 층 재귀 실행
    mid = in_arr.index(root)
    change_to_post(pre_arr[1:mid+1], in_arr[:mid])
    change_to_post(pre_arr[mid+1:], in_arr[mid+1:])
    print(root, end=" ")

change_to_post(pre_order, in_order)