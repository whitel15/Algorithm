from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    queue = deque()

    for i in range(n):
        if visited[i] == False:
            queue.append(i)
            visited[i] = True
            answer += 1

        while queue:
            k = queue.popleft()
            tmp = -1
            for j in computers[k]:
                tmp += 1
                if j == 1 and visited[tmp] == False:
                    queue.append(tmp)
                    visited[tmp] = True

    return answer