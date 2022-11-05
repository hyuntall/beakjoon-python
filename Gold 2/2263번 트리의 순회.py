import sys
sys.setrecursionlimit(10**6)

N = int(input())
in_order = list(map(int, sys.stdin.readline().split()))
post_order = list(map(int, sys.stdin.readline().split()))


post = [0]*(N+1)
for i in range(N):
    post[in_order[i]] = i

def change_to_post(post_start, post_end, in_start, in_end):
    if post_start>post_end or in_start>in_end:
        return

    # 후위 순회 리스트의 마지막 요소가 현재 층의 루트
    parents = post_order[post_end]
    print(parents, end=" ")
    # 루트 요소를 기준으로 나누어 다음 층 재귀 실행
    left = post[parents] - in_start
    right = in_end - post[parents]

    change_to_post(post_start, post_start+left-1, in_start, in_start+left-1)
    change_to_post(post_end-right, post_end-1, in_end-right+1, in_end)


change_to_post(0, N-1, 0, N-1)
