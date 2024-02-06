def solution(x):
    answer = True
    num = list(str(x))
    k = 0
    for i in range(len(num)):
        k += int(num[i])

    if x % k != 0:
        answer = False
    return answer