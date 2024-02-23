def solution(new_id):
    ans = ""
    giho = ["-", "_", "."]

    answer = new_id.lower()

    for i in range(len(answer)):
        if answer[i].isalpha() or answer[i].isdigit() or answer[i] in giho:
            ans += answer[i]

    chk = 0
    answer = ""

    for i in range(len(ans)):
        if ans[i] == "." and chk == 1:
            continue
        elif ans[i] == ".":
            chk = 1
            answer += ans[i]
        else:
            chk = 0
            answer += ans[i]

    if len(answer) > 0 and answer[0] == ".":
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == ".":
        answer == answer[:-1]

    if len(answer) == 0:
        answer = "a"

    if len(answer) >= 16:
        answer = answer[:15]

    if answer[-1] == ".":
        answer = answer[:-1]

    if len(answer) < 3:
        a = answer[-1]
        while len(answer) < 3:
            answer += a

    return answer