def solution(ingredient):
    answer = 0
    stack = []

    for i in range(len(ingredient)):
        if len(stack) < 3:
            stack.append(ingredient[i])
        else:
            if ingredient[i] == 1 and stack[-3:] == [1, 2, 3]:
                del stack[-3:]
                answer += 1
            else:
                stack.append(ingredient[i])

    return answer