from collections import deque


def solution(begin, target, words):
    answer = 0
    queue = deque()
    visit = [0 for _ in range(len(words))]

    queue.append((begin, 0))

    while queue:
        word, tmp = queue.popleft()

        for i in range(len(words)):
            cnt = 0
            for j in range(len(target)):
                if word[j] == words[i][j] and visit[i] == 0:
                    cnt += 1
                else:
                    chk = j
            if cnt == len(target) - 1 and words[i] == target:
                return tmp + 1
            elif cnt == len(target) - 1:
                queue.append((words[i], tmp + 1))
                visit[i] = 1

    return answer