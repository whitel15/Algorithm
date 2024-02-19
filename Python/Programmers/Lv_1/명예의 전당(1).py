def solution(k, score):
    answer = []
    mj = []

    for i in range(len(score)):
        if i < k:
            mj.append(score[i])
        else:
            if mj[-1] < score[i]:
                mj.pop()
                mj.append(score[i])
        mj.sort(reverse=True)
        answer.append(mj[-1])

    return answer