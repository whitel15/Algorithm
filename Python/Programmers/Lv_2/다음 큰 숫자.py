def solution(n):
    answer = 0

    x = bin(n)[2:]
    cnt1 = x.count("1")

    while True:
        n += 1
        y = bin(n)[2:]
        if cnt1 == y.count("1"):
            answer = n
            break

    return answer