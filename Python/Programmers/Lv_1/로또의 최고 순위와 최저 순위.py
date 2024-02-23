def solution(lottos, win_nums):
    answer = []

    count = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    cert = 0

    for i in lottos:
        if i in win_nums:
            cert += 1

    answer.append(count[cert + lottos.count(0)])
    answer.append(count[cert])

    return answer