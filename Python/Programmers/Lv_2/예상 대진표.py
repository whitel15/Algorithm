def solution(n, a, b):
    answer = 1
    x = (a + 1) // 2
    y = (b + 1) // 2

    while x != y:
        answer += 1
        x = (x + 1) // 2
        y = (y + 1) // 2

    return answer