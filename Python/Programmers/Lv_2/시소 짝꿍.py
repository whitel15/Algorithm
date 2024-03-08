def solution(weights):
    answer = 0

    weights.sort()

    dic = {}

    for i in weights:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for key, value in dic.items():
        if value > 1:
            answer += value * (value - 1) // 2

        for i in [2, 3 / 2, 4 / 3]:
            if key * i in dic:
                answer += value * dic[key * i]

    return answer