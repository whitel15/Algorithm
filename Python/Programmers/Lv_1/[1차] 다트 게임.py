def solution(dartResult):
    answer = 0

    three = []
    vonus = {"S": 1, "D": 2, "T": 3}
    chk = 0

    for i in dartResult:
        if i in vonus:
            three[-1] = three[-1] ** vonus[i]
            chk = 0
        elif i == "*":
            if len(three) >= 2:
                three[-2] *= 2
            three[-1] *= 2
            chk = 0
        elif i == "#":
            three[-1] *= -1
            chk = 0
        else:
            if chk:
                three[-1] = 10
                chk = 0
            else:
                three.append(int(i))
                chk = 1
    for i in three:
        answer += i

    return answer