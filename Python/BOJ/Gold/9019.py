import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    visited = [0 for _ in range(10001)]
    dq = deque()
    dq.append((a, ""))
    visited[a] = 1
    while dq:
        num, path = dq.popleft()
        if num == b:
            print(path)
            break

        D = num * 2 % 10000
        if num == 0:
            S = 9999
        elif num > 0:
            S = num - 1
        L = num // 1000 + (num % 1000) * 10
        R = num // 10 + (num % 10) * 1000

        if visited[D] == 0:
            visited[D] = 1
            dq.append((D, path + "D"))
        if visited[S] == 0:
            visited[S] = 1
            dq.append((S, path + "S"))
        if visited[L] == 0:
            visited[L] = 1
            dq.append((L, path + "L"))
        if visited[R] == 0:
            visited[R] = 1
            dq.append((R, path + "R"))