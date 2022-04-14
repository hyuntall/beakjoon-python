from sys import stdin
from collections import deque

M, N, H = map(int, input().split())
box = []
queue = deque([])

for i in range(H):
    floor = []
    for j in range(N):
        floor.append(list(map(int, stdin.readline().split())))
        for k in range(M):
            # 입력받은 값 중에 1이 있으면 queue에 넣어 검사 시작점으로 설정
            if floor[j][k] == 1:
                queue.append([i, j, k])
    box.append(floor)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while queue:
    x, y, z = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and box[nx][ny][nz] == 0:
            queue.append([nx, ny, nz])
            # 익은 토마토 주변 값들을 1씩 늘려준다
            # 하루씩 지나는 것을 표현
            box[nx][ny][nz] = box[x][y][z] + 1

cnt = 0
for i in box:
    for j in i:
        for k in j:
            if k == 0:
                # 박스에 익지않은 토마토가 있으면 -1
                print(-1)
                exit(0)
        # 박스를 검사하면서 가장 크게 지난 날짜를 비교
        cnt = max(cnt, max(j))
print(cnt - 1)
