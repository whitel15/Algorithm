def solution(n):
    answer = 1

    for i in range(1, n):
        num = i
        for j in range(i + 1, n):
            num += j
            if num == n:
                answer += 1
                break
            elif num > n:
                break

    return answer