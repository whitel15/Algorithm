from collections import Counter

def solution(X, Y):
    answer = ''
    ans = []

    a = dict(Counter(X))
    b = dict(Counter(Y))

    for i in a:
        if i in b:
            for _ in range(min(a[i], b[i])):
                ans.append(i)

    ans.sort(reverse=True)

    if len(ans) == 0:
        return "-1"

    if len(ans) == ans.count("0"):
        return "0"

    return answer.join(ans)