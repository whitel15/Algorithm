def solution(k, m, score):
    answer = 0
    idx = m - 1
    if len(score) < m:
        return 0

    score.sort(reverse=True)

    while idx < len(score):
        answer += m * score[idx]
        idx += m

    return answer