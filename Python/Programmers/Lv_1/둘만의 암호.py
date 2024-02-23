def solution(s, skip, index):
    answer = ''

    for i in s:
        cnt = 0
        w = i
        while cnt < index:
            if ord(w) + 1 > 122:
                w = "a"
            else:
                w = chr((ord(w) + 1))
            if w not in skip:
                cnt += 1

        answer += w

    return answer