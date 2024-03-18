def solution(data, col, row_begin, row_end):
    ss = []

    data.sort(key=lambda x: (x[col - 1], -x[0]))

    for i in range(row_begin, row_end + 1):
        s = 0
        for j in data[i - 1]:
            s += j % i
        ss.append(s)
    answer = ss[0]
    for i in ss[1:]:
        answer ^= i

    return answer