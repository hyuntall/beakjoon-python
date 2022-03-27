# 입력받은 값을 -를 기준으로 나눈다
a = input().split('-')
b = []

# 나눈 식을 각각 + 해준다
for i in a:
    plus = 0
    s = i.split('+')
    for j in s:
        plus += int(j)
    # +를 각각 더해 리스트에 저장한다.
    b.append(plus)

answer = b[0]
# 첫번째 값에서 각각 더해진 값을 빼준다.
for i in range(1, len(b)):
    answer -= b[i]

print(answer)