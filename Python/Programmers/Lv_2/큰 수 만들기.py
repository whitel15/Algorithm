def solution(number, k):
    stack = [number[0]]

    for i in number[1:]:
        while stack and i > stack[-1] and k > 0:
            stack.pop()
            k -= 1
        stack.append(i)

    if k:
        stack = stack[:-k]

    return "".join(stack)