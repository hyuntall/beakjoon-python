import math

com_div, com_mul = map(int, input().split())


# com_div의 배수이자, com_mul의 약수인 리스트 반환
def getDivisor(n):
    arr = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % com_div == 0:
                arr.append(i)
            if i ** 2 != n and (n // i) % com_div == 0:
                arr.append(n // i)
    return sorted(arr)


# com_div의 배수이자, com_mul의 약수인 리스트 반환
div_arr = getDivisor(com_mul)

# A, B의 최소 합을 구하기 위해 최대값 설정
minSum = com_mul * 2
A = div_arr[0]
B = div_arr[-1]

# 투 포인터를 사용하여 A와 B 탐색
for i in range(len(div_arr)):
    for j in range(i, len(div_arr) - 1):
        # A와 B의 최소공배수가 com_mul 이라면
        if math.lcm(div_arr[i], div_arr[j]) == com_mul:
            # A+B의 값이 최소인지 확인
            if minSum > div_arr[i] + div_arr[j]:
                A, B = div_arr[i], div_arr[j]
                minSum = A + B
print(A, B)
