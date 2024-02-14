def solution(n):
    answer = 0
    n3 = ""

    while n > 0:
        remain = n % 3
        n //= 3
        n3 += str(remain)

    answer = int(n3, 3)

    return answer