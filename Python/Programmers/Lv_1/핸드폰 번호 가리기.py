def solution(phone_number):
    answer = ''

    a = len(phone_number)

    for i in range(a):
        if i >= a - 4:
            answer += phone_number[i]
        else:
            answer += "*"

    return answer