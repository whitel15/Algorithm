def solution(num):
    answer = -1

    for i in range(500):
        if num == 1:
            return i
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1

    return answer