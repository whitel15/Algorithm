def solution(clothes):
    answer = 0
    dic = {}
    s = 1

    for i in range(len(clothes)):
        if clothes[i][1] in dic:
            dic.setdefault(clothes[i][1], []).append(clothes[i][0])
        else:
            dic[clothes[i][1]] = [clothes[i][0]]

    for i in dic:
        a = len(dic[i]) + 1
        s *= a

    answer = s - 1

    return answer