from itertools import combinations

def solution(numbers):
    answer = []

    for i in list(combinations(numbers, 2)):
        answer.append(i[0] + i[1])

    return sorted(list(set(answer)))