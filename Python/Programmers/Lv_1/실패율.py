from collections import Counter

def solution(N, stages):
    answer = []
    stage = [0 for _ in range(N + 2)]
    ans = []

    c = Counter(stages)

    for i in c:
        stage[i] = c[i]

    s = 0

    for i in range(N + 1, 0, -1):
        if i == N + 1:
            s = stage[i]
        else:
            s += stage[i]
            if s == 0:
                ans.append([i, 0])
            else:
                ans.append([i, stage[i] / s])
    ans.sort(key=lambda x: (-x[1], x[0]))

    for i in range(len(ans)):
        answer.append(ans[i][0])

    return answer