def solution(n, t, m, p):
    answer = ''

    num = m * (t - 1) + p
    nu = "0"

    for i in range(num):
        s = ""
        while i > 0:
            remainder = i % n
            i //= n
            if remainder >= 10:
                s = chr(remainder + 55) + s
            else:
                s = str(remainder) + s
        nu += s

    for i in range(p - 1, m * (t - 1) + p, m):
        answer += nu[i]

    return answer