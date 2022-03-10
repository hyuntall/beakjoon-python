N, M = map(int, input().split())
nArr = []
mArr = []

nArr = [list(map(int, list(input()))) for _ in range(N)]
mArr = [list(map(int, list(input()))) for _ in range(N)]

cnt = 0
# 3*3 칸만큼 값을 뒤집는 함수
def reverse(arr, x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            arr[i][j] = 1 - arr[i][j]

for i in range(N-2):
    for j in range(M-2):
        if nArr[i][j] != mArr[i][j]:
            reverse(nArr, i, j)
            cnt += 1

# 행렬 A와 B가 같은지 검사
def check():
    for i in range(N):
        for j in range(M):
            if nArr[i][j] != mArr[i][j]:
                return False
    return True

print(cnt if check() else -1)

# 총평:
# 브루트포스 문제 정말 귀찮다...