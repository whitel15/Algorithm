def solution(arr):
    answer = []

    for i in arr:
        if len(answer) == 0:
            answer.append(i)
        else:
            top = answer.pop()
            if i != top:
                answer.append(top)
                answer.append(i)
            else:
                answer.append(top)

    return answer