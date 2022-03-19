from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())

# 망가진 버튼이 없으면 리스트 입력 받지 않음
if M > 0:
    broken_button = list(map(str, input().split()))
else:
    broken_button = []

# 이동하려는 채널이 시작 채널과 같으면 0
if N == 100:
    print(0)
else:
    # 최대 횟수는 목표 채널까지 +만 눌렀을 때의 횟수
    minCnt = abs(N - 100)
    # 입력 제한은 500000이지만
    # 1부터 500000까지의 차이와
    # 1000000부터 500000까지의 차이도 고려해야함
    for num in range(1000001):
        possible = True
        # 모든 경우의 수를 검사하면서
        # 해당 숫자가 고장난 버튼의 숫자인지 검사
        for i in str(num):
            if i in broken_button:
                possible = False
                break
        # 가능한 숫자라면
        if possible:
            # 최소 횟수는 숫자버튼을 누르는 횟수와 +혹은-를 누르는 횟수의 합
            minCnt = min(minCnt, len(str(num)) + abs(num - int(N)))

    print(minCnt)