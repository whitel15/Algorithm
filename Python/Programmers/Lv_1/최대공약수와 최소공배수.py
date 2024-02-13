def solution(n, m):
    answer = []

    a = min(n, m)

    for i in range(a, 0, -1):
        if m % i == 0 and n % i == 0:
            answer.append(i)
            break

    answer.append(n * m // answer[0])

    return answer