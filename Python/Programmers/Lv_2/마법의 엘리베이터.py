def solution(storey):
    answer = 0
    k = len(str(storey))

    while k > 0:
        if k == 1:
            if storey > 5:
                answer += 11 - storey
            else:
                answer += storey
        elif storey % 10 > 5:
            answer += 10 - storey % 10
            storey = storey // 10 + 1
        elif storey % 10 == 5 and (storey % 100) // 10 > 4:
            answer += 5
            storey = storey // 10 + 1
        else:
            answer += storey % 10
            storey = storey // 10
        k -= 1

    return answer