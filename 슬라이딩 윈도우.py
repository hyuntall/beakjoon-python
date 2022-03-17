drinks = []
N = 10
for _ in range(N):
    num, ca, ta = map(int, input().split())
    drinks.append([num, ca, ta])

window = 3
maxTaCa = 0
point = 0
while point < N-2:
    sumCa = 0
    sumTa = 0
    for i in range(window):
        sumCa += drinks[point+i][1]
        sumTa += drinks[point+i][2]
    if maxTaCa < sumTa-sumCa:
        a, b, c = point, point+1, point+2
        maxTa = sumTa
        minCa = sumCa
    point += 1

print(f"{a} {b} {c}의 타우린 합은 {maxTa}, 카페인 합은 {minCa}로 가장 효과가 좋습니다.")