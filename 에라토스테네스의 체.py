def era(n):

    # 0번 인덱스부터 시작하기 때문에 n+1
    prime_range = n+1
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정
    prime_list = [True]*prime_range

    sqrt = int(n**0.5)
    for i in range(2, sqrt+1):
        # i가 소수인 경우
        if prime_list[i]:
            # i 이후 i의 배수들을 False 판정
            for j in range(i+i, prime_range,i):
                prime_list[j] = False
    return prime_list

def answer(N):
    prime = []
    prime_list = era(N)
    for i in range(2, len(prime_list)):
        if prime_list[i]:
            prime.append(i)
        if sum(prime) == N:
            print(f"연속된 소수 {prime}의 합은 {N}입니다.")
            break
        elif sum(prime) > N:
            print(f"연속된 소수의 합으로 {N}을 만들 수 없습니다.")
            break

answer(41)
answer(20)