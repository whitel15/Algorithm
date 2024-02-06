def solution(n):
    answer = []

    for i in range(len(str(n))):
        answer.append(int(str(n)[len(str(n)) - 1 - i]))

    return answer