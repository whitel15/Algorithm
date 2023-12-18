def solution(numbers, target):
    answer = 0
    leaves = [0]

    for i in numbers:
        tmp = []
        for j in leaves:
            tmp.append(j + i)
            tmp.append(j - i)
        leaves = tmp

    for i in leaves:
        if i == target:
            answer += 1

    return answer