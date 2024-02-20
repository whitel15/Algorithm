from itertools import combinations

def solution(nums):
    answer = 0

    for i in list(combinations(nums, 3)):
        num = sum(i)
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                break
        else:
            answer += 1

    return answer