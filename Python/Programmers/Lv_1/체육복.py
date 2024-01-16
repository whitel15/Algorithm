def solution(n, lost, reserve):
    answer = n - len(lost)

    lost.sort()
    reserve.sort()

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                answer += 1
                lost[i] = -1
                reserve[j] = -5

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] - 1 == reserve[j]:
                answer += 1
                reserve[j] = -5
                break
            elif lost[i] + 1 == reserve[j]:
                answer += 1
                reserve[j] = -5
                break

    return answer