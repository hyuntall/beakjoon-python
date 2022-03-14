# 좌, 상, 우, 하 방향 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, cnt, visited):
    # 현재 위치를 visited에 추가
    visited.append([x, y])

    # 현재 위치가 집(오른쪽 위)라면 딕셔너리에 cnt += 1
    if x == 0 and y == C-1:
        if cnt in dict:
            dict[cnt] += 1
        else:
            dict[cnt] = 1
        return

    # 상하좌우 모든 방향에 대해
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 이동하려는 곳이 범위 내에 있고, T가 아니고, 방문했던 적이 없다면
        if 0 <= nx < R and 0 <= ny < C and load[nx][ny] != 'T' and [nx, ny] not in visited:
            # 이동할 위치와, cnt+1, 각각의 방문 내역을 따로 주어 재귀 호출
            dfs(nx, ny, cnt + 1, visited + [nx, ny])


R, C, K = map(int, input().split())
load = []
dict = {}

for _ in range(R):
    load.append(input())

# 시작 위치(왼쪽 아래)에서 함수 호출
dfs(R-1, 0, 1, [])

# 거리가 K인 경우의 수가 있으면 가짓수 출력
print(dict[K] if K in dict else 0)
