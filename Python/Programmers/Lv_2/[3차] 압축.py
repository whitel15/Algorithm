def solution(msg):
    answer = []
    word = {}

    for i in range(26):
        word[chr(65 + i)] = i + 1

    idx = 0

    while True:
        if idx == len(msg) - 1:
            answer.append(word[msg[idx]])
            return answer
        for i in range(idx + 1, len(msg) + 1):
            if i == len(msg):
                if msg[idx:] in word:
                    answer.append(word[msg[idx:]])
                    return answer
                else:
                    answer.append(word[msg[idx:-1]])
                    answer.append(word[msg[-1]])
                    return answer

            if i != idx + 1:
                if msg[idx:i] in word:
                    continue
                else:
                    answer.append(word[msg[idx:i - 1]])
                    word[msg[idx:i]] = len(word) + 1
                    idx = i - 1
                    break

    return answer
