from sys import stdin

N = int(input())
# 맨 처음 세개의 숫자를 입력받아 DP의 초기 값을 설정한다.
arr = list(map(int, stdin.readline().split()))
maxDP = arr
minDP = arr
for _ in range(N - 1):
    arr = list(map(int, stdin.readline().split()))
    # 세가지 값을 입력받을 때마다, DP에 새롭게 갱신한다.
    maxDP = [arr[0] + max(maxDP[0], maxDP[1]), arr[1] + max(maxDP), arr[2] + max(maxDP[1], maxDP[2])]
    minDP = [arr[0] + min(minDP[0], minDP[1]), arr[1] + min(minDP), arr[2] + min(minDP[1], minDP[2])]

print(max(maxDP), min(minDP))

# 슬라이딩 윈도우란
# dp에서 메모이제이션을 할 때, 사용하지 않는 값을 저장하지 않고
# 배열을 새롭게 계속 갱신해주는 것