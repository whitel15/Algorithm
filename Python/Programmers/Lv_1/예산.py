def solution(d, budget):
    answer = 0
    cnt = 0
    d.sort()

    for i in d:
        cnt += i
        if cnt <= budget:
            answer += 1
        else:
            break
    return answer