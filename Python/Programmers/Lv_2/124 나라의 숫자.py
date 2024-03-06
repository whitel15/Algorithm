def solution(n):
    answer = ""

    while n:
        t = n % 3
        if t == 0:
            t = 4
            n -= 1
        answer = str(t) + answer
        n //= 3

    return answer