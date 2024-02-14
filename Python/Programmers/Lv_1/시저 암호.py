def solution(s, n):
    answer = ''

    for i in s:
        if i == " ":
            answer += " "
        elif ord(i) <= 90:
            if ord(i) + n % 26 > 90:
                answer += chr(ord(i) + n % 26 - 26)
            else:
                answer += chr(ord(i) + n % 26)
        else:
            if ord(i) + n % 26 > 122:
                answer += chr(ord(i) + n % 26 - 26)
            else:
                answer += chr(ord(i) + n % 26)
    return answer