def solution(s):
    answer = []

    cnt = 0
    num = 0

    while True:
        if s == "1":
            answer.append(cnt)
            answer.append(num)
            break

        cnt += 1
        ns = ""

        for i in range(len(s)):
            if s[i] == "1":
                ns += s[i]
            else:
                num += 1

        s = bin(len(ns))[2:]

    return answer