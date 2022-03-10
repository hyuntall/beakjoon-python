n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())

# 고쳐야할 최대 값
answer = n*m

# 칸마다 검사 기준 색을 바꾸는 함수
def changeColor(color):
    if color=='W':
        return 'B'
    else:
        return 'W'

for _ in range(2):
    # W시작, B시작 둘 다 비교
    if _ == 0:
        start = 'W'
    else:
        start = 'B'
    # 판의 크기가 8*8이상일 수 있기 때문에
    # 자를 수 있는 8*8의 모든 경우의 수
    for i in range(n-7):
        for j in range(m-7):
            cnt = 0
            temp = start
            for row in board[i:i+8]:
                for col in row[j:j+8]:
                    # 칸마다 비교하여 다시 칠해야 하면 +1
                    if col != temp:
                        cnt += 1
                    # 기준 색 변경
                    temp = changeColor(temp)
                # 다음 줄로 넘어가면 기준 색 유지하기 위해 다시 변경
                temp = changeColor(temp)
            # 모든 경우의 수 비교하여 최솟값 출력
            answer = min(cnt, answer)

print(answer)

# 총평:
# 이 문제는 사실 옛날에 풀었다가 포기했던 문제였다.
# 오랜만에 다시 도전하여 브루트포스 방식으로 접근했더니
# 코드 작성 도중에 반복문이 많아 다소 헷갈리는 것을 제외하고
# 그렇게 어렵지 않은 문제였다.