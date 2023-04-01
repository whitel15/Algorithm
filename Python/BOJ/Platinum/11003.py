from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
string = list(map(int, input().split()))

d = deque()

for i in range(N):
    while d and d[-1][0] > string[i]:
        d.pop()
    d.append((string[i], i))
    if d[0][1] <= i - L:
        d.popleft()
    print(d[0][0], end=" ")