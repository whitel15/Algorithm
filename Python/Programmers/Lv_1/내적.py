def solution(a, b):
    sl = [a[i] * b[i] for i in range(len(a))]

    answer = sum(sl)

    return answer