from collections import deque

T = int(input())
for _ in range(T):
    func = input()
    N = int(input())
    # 입력받은 값을 배열로 저장하기 위해 양 옆 괄호를 자르고 ,로 끊어준다
    arr = input()[1:-1].split(',')
    arr = deque(arr)

    # R함수에 관한 플래그
    reverse = 0
    # error 플래그
    error = 0

    if N==0:
        arr = []

    # 모든 함수를 실행
    for f in func:
        # R 함수가 실행되면 reverse 변수를 뒤집어준다.
        if f == 'R':
            reverse = 1 - reverse
        else:
            # 배열이 비어있으면 에러
            if not arr:
                error = 1
                break

            # 배열이 뒤집어 졌을 때 pop,
            # 뒤집어지지 않았을 때 leftpop으로
            # 배열의 맨 앞요소를 출력한다.
            if reverse:
                arr.pop()
            else:
                arr.popleft()

    # 에러가 났으면 error 출력
    if error:
        print('error')
    else:
        # 배열이 뒤집힌 상태면 뒤집어 출력
        if reverse:
            arr.reverse()
            print(f"[{','.join(arr)}]")
        # 그렇지 않다면 그냥 출력
        else:
            print(f"[{','.join(arr)}]")