import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1111111)

t = int(input())
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(t):
    w, h = map(int, input().split())
    building = [[] for _ in range(h)]
    Fvisited = [[0 for _ in range(w)] for _ in range(h)]
    Svisited = [[0 for _ in range(w)] for _ in range(h)]
    fire = []
    sg = []
    ans = "IMPOSSIBLE"
    for i in range(h):
        line = input().strip()
        for j in line:
            building[i].append(j)

    for i in range(h):
        for j in range(w):
            if building[i][j] == "*":
                fire.append((i, j))
            elif building[i][j] == "@":
                sg.append((i, j))
                Svisited[i][j] = 1


    dq = deque()
    dq.append((fire, sg, 0))

    for i in range(len(fire)):
        Fvisited[fire[i][0]][fire[i][1]] = 1

    while dq:
        if ans != "IMPOSSIBLE":
            break
        f, s, cnt = dq.popleft()
        nf = []
        ns = []

        for i in range(len(f)):
            for j in range(4):
                fx = f[i][0] + direction[j][0]
                fy = f[i][1] + direction[j][1]
                if 0 <= fx < h and 0 <= fy < w and building[fx][fy] != "#" and Fvisited[fx][fy] == 0:
                    building[fx][fy] = "*"
                    Fvisited[fx][fy] = 1
                    nf.append((fx, fy))

        for i in range(len(s)):
            for j in range(4):
                sx = s[i][0] + direction[j][0]
                sy = s[i][1] + direction[j][1]
                if sx < 0 or sx >= h or sy < 0 or sy >= w:
                    ans = cnt + 1
                    break
                elif building[sx][sy] == "." and Svisited[sx][sy] == 0:
                    Svisited[sx][sy] = 1
                    ns.append((sx, sy))

        if len(ns) == 0:
            break
        dq.append((nf, ns, cnt + 1))


    print(ans)