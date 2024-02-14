def solution(s):
    answer = ''
    chk = 0

    for i in range(len(s)):
        if s[i] == " ":
            chk = 0
            answer += s[i]
        elif chk % 2 == 0:
            answer += s[i].upper()
            chk += 1
        else:
            answer += s[i].lower()
            chk += 1
    return answer