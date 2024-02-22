def solution(s):
    answer = 0

    first = s[0]
    same = 1
    Nsame = 0

    for i in range(1, len(s)):
        if s[i] == first:
            same += 1
        else:
            Nsame += 1

        if same == Nsame:
            answer += 1
            same = 0
            Nsame = 0
            if i + 1 < len(s):
                first = s[i + 1]

    if answer == 0 or same != 0:
        answer += 1

    return answer