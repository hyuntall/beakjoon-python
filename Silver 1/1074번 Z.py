N, r, c = map(int, input().split())
n = 2**N
cnt = 0
while n > 0:
    n //= 2
    # r, c가 좌상단에 있을 때
    if r < n and c < n:
        cnt += n*n * 0
    # r, c가 우상단에 있을 때
    elif r < n and c >= n:
        cnt += n*n * 1
        c -= n
    # r, c가 좌하단에 있을 때
    elif r >= n and c < n:
        cnt += n*n * 2
        r -= n
    # r. c가 우하단에 있을 때
    elif r >= n and c >= n:
        cnt += n*n * 3
        c -= n
        r -= n

print(cnt)

# 총평:
# 2의 n제곱 x 2의 n제곱으로 구성된 판을 4등분 하면
# 각 판의 시작점이 2(n-1) * 2(n-1)만큼 차이가 난다
# r,c가 어느 방향에 존재하는지에 따라 기본 시작 횟수를 알 수 있다.
# 4등분을 반복하면서 횟수를 더하다 보면 답이 나온다.
# 처음에 재귀함수로 접근하려했을 때 답이 나오지 않아
# 문제를 잘 읽어보니 4등분 할 때마다 규칙나타남을 알 수 있었다.