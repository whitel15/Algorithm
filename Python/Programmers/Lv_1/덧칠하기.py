def solution(n, m, section):
    answer = 1
    now = section[0] + m

    for i in range(len(section)):
        if section[i] < now:
            continue
        else:
            now = section[i] + m
            answer += 1

    return answer