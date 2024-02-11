def solution(s):
    answer = ''
    a = []
    for i in s:
        a.append(i)
    a.sort(key = lambda x:ord(x), reverse = True)
    for i in a:
        answer += i
    return answer