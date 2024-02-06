def solution(n):
    answer = 1

    while n != 1:
        if n % 2:
            answer += 1
            n = (n - 1) // 2
        else:
            n = n // 2

    return answer