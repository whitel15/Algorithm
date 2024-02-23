def solution(keymap, targets):
    answer = []
    dic = {}

    for i in keymap:
        for j in range(len(i)):
            if i[j] not in dic or j < dic[i[j]]:
                dic[i[j]] = j + 1

    for i in targets:
        ans = 0
        for j in i:
            if j not in dic:
                ans = -1
                break
            else:
                ans += dic[j]

        answer.append(ans)

    return answer