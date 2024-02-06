def solution(s):
    a = []

    for i in range(len(s)):
        if len(a) == 0:
            a.append(s[i])
        elif a[-1] == s[i]:
            a.pop()
        else:
            a.append(s[i])

    if len(a):
        return 0
    else:
        return 1