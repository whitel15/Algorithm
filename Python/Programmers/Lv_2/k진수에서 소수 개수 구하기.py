def solution(n, k):
    answer = 0
    result = ""

    while n > 0:
        remainder = n % k
        result = str(remainder) + result
        n //= k

    find = result.split("0")

    for i in find:
        if i != "":
            i = int(i)
            a = 1
            for j in range(2, int(i ** (1 / 2)) + 1):
                if i % j == 0:
                    a = 0
                    break
            if i != 1 and a:
                answer += 1

    return answer