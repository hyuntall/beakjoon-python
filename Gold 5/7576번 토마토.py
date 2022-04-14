from sys import stdin
from collections import deque

M, N= map(int, input().split())
queue = deque([])

box = []
for i in range(N):
    box.append(list(map(int, stdin.readline().split())))
    for j in range(M):
        # 입력받은 값 중에 1이 있으면 queue에 넣어 검사 시작점으로 설정
        if box[i][j] == 1:
            queue.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
            queue.append([nx, ny])
            # 익은 토마토 주변 값들을 1씩 늘려준다
            # 하루씩 지나는 것을 표현
            box[nx][ny] = box[x][y] + 1

cnt = 0
for i in box:
    for j in i:
        if j == 0:
            # 박스에 익지않은 토마토가 있으면 -1
            print(-1)
            exit(0)
    # 박스를 검사하면서 가장 크게 지난 날짜를 비교
    cnt = max(cnt, max(i))
print(cnt - 1)
