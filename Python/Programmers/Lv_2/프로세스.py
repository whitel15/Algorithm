def solution(priorities, location):
    answer = 0

    k = list(enumerate(priorities))

    while k:
        t = k.pop(0)
        for i in k:
            if t[1] < i[1]:
                k.append(t)
                break
            else:
                if i == k[-1]:
                    if t[0] == location:
                        answer = len(priorities) - len(k)

    if answer == 0:
        answer = len(priorities)

    return answer