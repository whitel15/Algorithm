def solution(friends, gifts):
    answer = 0
    present = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    jisu = [[0 for _ in range(3)] for _ in range(len(friends))]
    nextM = [0 for _ in range(len(friends))]

    for i in range(len(gifts)):
        for j in range(len(friends)):
            if gifts[i].split(" ")[0] == friends[j]:
                for z in range(len(friends)):
                    if gifts[i].split(" ")[1] == friends[z]:
                        present[j][z] += 1
                        jisu[j][0] += 1
                        jisu[z][1] += 1

    for i in range(len(friends)):
        jisu[i][2] = jisu[i][0] - jisu[i][1]

    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            if present[i][j] > present[j][i]:
                nextM[i] += 1
            elif present[i][j] < present[j][i]:
                nextM[j] += 1
            else:
                if jisu[i][2] > jisu[j][2]:
                    nextM[i] += 1
                elif jisu[i][2] < jisu[j][2]:
                    nextM[j] += 1

    answer = max(nextM)

    return answer