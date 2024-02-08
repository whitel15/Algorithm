def solution(s):
    answer = 0
    bracket = {"(": ")", "[": "]", "{": "}"}

    for i in range(len(s)):
        stack = []
        find = True
        for j in range(len(s)):
            if s[j] in bracket:
                stack.append(s[j])
            elif len(stack) == 0 or bracket[stack[-1]] != s[j]:
                find = False
                break
            else:
                stack.pop()
        if find and len(stack) == 0:
            answer += 1
        s = s[1:] + s[0]

    return answer