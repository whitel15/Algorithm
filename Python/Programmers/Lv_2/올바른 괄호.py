def solution(s):
    answer = True
    a = 0
    b = 0
    t = []

    for i in s:
        t.append(i)

    while t:
        dir = t.pop()
        if dir == ")":
            a += 1
        else:
            b += 1
            if a < b:
                answer = False
                break
            else:
                a -= 1
                b -= 1

    if a != b:
        answer = False

    return answer