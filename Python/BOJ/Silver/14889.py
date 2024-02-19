import copy
import sys
input = sys.stdin.readline

n = int(input())
sl = []
path = []
ab = 1000
visited = [0 for _ in range(n+1)]
for i in range(n):
    sl.append(list(map(int, input().split())))


def bfs(TeamMember):
    global ab
    score = 0
    score2 = 0
    for i in TeamMember:
        for j in TeamMember:
            score += sl[i-1][j-1]
    nt = [i for i in range(1, n+1)]
    for i in TeamMember:
        nt.remove(i)
    for i in nt:
        for j in nt:
            score2 += sl[i-1][j-1]
    ab = min(ab, abs(score - score2))


def make_team_with_one(idx):
    global n
    global path
    if len(path) == n/2:
        bfs(path)
        return
    for i in range(idx, n+1):
        if i not in path:
            path.append(i)
            make_team_with_one(i + 1)
            path.pop()

make_team_with_one(1)

print(ab)