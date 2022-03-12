L, R = map(str, input().split())

# L과 R의 자릿수가 다르면 반드시 8시 없는 구간이 존재
if len(L) != len(R):
    print(0)
else:
    cnt = 0
    for i in range(len(R)):
        # L과 R의 각 자릿수가 같고, 8이면 +1
        if L[i] == R[i]:
            if L[i] == '8':
                cnt += 1
        else:
            break
    print(cnt)
# 총평:
# 첫번째 시도
"""
answer = len(str(R))
for i in range(L, R+1):
    if '8' not in str(i):
        print(0)
        exit()
    answer = min(answer, str(i).count('8'))
print(answer)
"""
# 당연하게도 시간 초과가 나왔다.
# 각 자릿수를 비교하는 개념으로 접근했을 때 풀 수 있었다.