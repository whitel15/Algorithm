from collections import deque

def solution(x, y, n):
    answer = -1
    visited = [0 for _ in range(y+1)]
    dq = deque()
    dq.append((x, 0))
    visited[x] = 1
    while dq:
        num, cnt = dq.popleft()
        if num == y:
            answer = cnt
            break
        if num + n <= y and visited[num + n] == 0:
            visited[num + n] = 1
            dq.append((num+n , cnt + 1))
        if num * 2 <= y and visited[num * 2] == 0:
            visited[num * 2] = 1
            dq.append((num * 2, cnt + 1))
        if num * 3 <= y and visited[num * 3] == 0:
            visited[num * 3] = 1
            dq.append((num * 3, cnt + 1))
    return answer