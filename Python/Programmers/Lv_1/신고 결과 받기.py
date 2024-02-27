def solution(id_list, report, k):
    answer = [0] * len(id_list)
    id = {}

    for i in id_list:
        id[i] = []

    for i in set(report):
        a, b = i.split(" ")
        id[b].append(a)

    for key, value in id.items():
        if len(value) >= k:
            for i in value:
                answer[id_list.index(i)] += 1

    return answer