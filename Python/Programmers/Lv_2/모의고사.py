def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for i in range(len(answers)):
        if answers[i] == one[i % 5]:
            score[0] += 1
        if answers[i] == two[i % 8]:
            score[1] += 1
        if answers[i] == three[i % 10]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result