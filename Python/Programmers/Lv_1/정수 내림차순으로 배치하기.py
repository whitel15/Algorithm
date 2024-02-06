def solution(n):
    ans = ""
    answer = list(str(n))
    answer.sort(reverse=True)

    for i in answer:
        ans += str(i)
    return int(ans)