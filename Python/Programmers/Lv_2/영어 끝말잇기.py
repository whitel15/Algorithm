def solution(n, words):
    answer = []
    word = {}

    for i in range(len(words)):
        if i == 0:
            word[words[i]] = 1
        elif words[i] not in word and words[i][0] == words[i - 1][-1]:
            word[words[i]] = 1
        else:
            if (i + 1) % n == 0:
                answer.append(n)
                answer.append((i + 1) // n)
            else:
                answer.append((i + 1) % n)
                answer.append((i + 1) // n + 1)

            return answer

    answer.append(0)
    answer.append(0)

    return answer