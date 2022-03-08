from sys import stdin

n = int(input())
p = list(map(int, input().split()))
s = list(map(int, stdin.readline().split()))

# 카드를 섞어 0 1 2 0 1 2...로 만들기 위해
# 0 1 2...로 이루어진 answer 생성
answer = [i%3 for i in range(n)]
temp = p

# i번째 카드를 s[i]번쨰로 섞는 함수
def shuffle(list, shup):
    arr = [0]*n
    for i in range(n):
        arr[shup[i]] = list[i]
    return arr

cnt = 0
# 카드 섞기
while p != answer:
    p = shuffle(p, s)
    cnt += 1
    # 섞은 카드가 초기 값과 같아지면
    # 0, 1, 2를 만들 수 없기에 -1 반환
    if p == temp:
        print(-1)
        exit()

print(cnt)

# 총평:
# 문제를 너무 복잡하게 생각했던 것 같다.
# 0 1 2 3 4...를 입력받은 s에 맞게 될 때까지 셔플한다는 접근했을 땐 정답이 나오지 않았다.
# 반대로 입력받은 s를 0, 1, 2가 되도록 섞는 관점으로 접근한 결과 해결할 수 있었다.
# 아직 골드는 조금 벅찬 것 같다.