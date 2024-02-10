def solution(name, yearning, photo):
    answer = []

    dic = {}

    for i in range(len(name)):
        dic[name[i]] = yearning[i]

    for i in range(len(photo)):
        a = 0
        for j in photo[i]:
            if j in dic:
                a += dic[j]
        answer.append(a)

    return answer