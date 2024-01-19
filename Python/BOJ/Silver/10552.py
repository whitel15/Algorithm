from collections import deque
import sys
input = sys.stdin.readline

n, m, p = map(int, input().split())
old = []
hateDic = {}
cnt = 0
visited = [0 for _ in range(m+1)]

for i in range(n):
    like, hate = map(int, input().split())
    if hate not in hateDic:
        hateDic[hate] = like

while True:
    now_ch = hateDic.get(p, -1)

    if now_ch == -1:
        print(cnt)
        break

    if visited[now_ch] != 0:
        print(-1)
        break

    visited[now_ch] = 1
    p = now_ch
    cnt += 1