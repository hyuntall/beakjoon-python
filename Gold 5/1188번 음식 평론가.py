N, M = map(int, input().split())

# a와 b의 최대 공약수
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

# 최악의 경우 M-1번 잘라야 함
print(M - gcd(N, M))
