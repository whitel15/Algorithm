def solution(p):
    answer = ''

    if len(p) == 0:
        return p

    u, v = divide(p)

    if chkRight(u):
        return u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        for i in u[1:len(u) - 1]:
            if i == "(":
                answer += ")"
            else:
                answer += "("
        return answer


def chkRight(s):
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return True


def divide(s):
    a, b = 0, 0
    for i in range(len(s)):
        if s[i] == "(":
            a += 1
        else:
            b += 1
        if a == b:
            return s[:i + 1], s[i + 1:]
