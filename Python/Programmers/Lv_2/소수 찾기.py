from itertools import permutations


def solution(numbers):
    answer = []
    num = [i for i in numbers]
    per = []

    for i in range(len(numbers)):
        per += list(permutations(num, i + 1))

    new_num = [int(("").join(p)) for p in per]

    for i in new_num:
        if i < 2:
            continue
        check = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                check = False
                break
        if check:
            answer.append(i)

    return len(set(answer))