def solution(participant, completion):
    dic = {}
    answer = " "

    for i in participant:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for i in completion:
        if i in dic:
            dic[i] -= 1

    for key, value in dic.items():
        if value > 0:
            answer = key
            break

    return answer