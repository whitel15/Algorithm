import itertools

def solution(orders, course):
    answer = []

    for i in course:
        dic = {}
        m = 2
        for j in orders:
            for z in list(itertools.combinations(j, i)):
                word = ""
                for k in z:
                    word += k
                word = "".join(sorted(word))
                if word in dic:
                    dic[word] += 1
                else:
                    dic[word] = 1
        for key, value in dic.items():
            m = max(m, value)
        for key, value in dic.items():
            if value == m:
                answer.append(key)
    answer.sort()

    return answer