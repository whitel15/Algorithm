def solution(order):
    answer = 0
    idx = 0
    i = 1
    stack = []

    while i <= len(order) + 1:

        if i < len(order) and i == order[idx]:
            answer += 1
            idx += 1
            i += 1
        elif stack and stack[-1] == order[idx]:
            while stack and stack[-1] == order[idx]:
                stack.pop()
                answer += 1
                idx += 1
        else:
            stack.append(i)
            i += 1

    return answer