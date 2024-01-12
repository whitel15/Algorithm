import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
r, c, t = map(int, input().split())
room = []
dir0 = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dir1 = [(-1, 0), (0, -1), (1, 0), (0, 1)]
dir2 = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dir3 = [(1, 0), (0, 1), (-1, 0), (0, -1)]

cnt = 0

for _ in range(n):
    room.append(list(map(int, input().strip().split())))


def clean(x, y, d):
    global cnt

    if room[x][y] == 0:
        room[x][y] = 2
        cnt += 1

    chk = False

    for i in range(4):
        dx = x + dir0[i][0]
        dy = y + dir0[i][1]
        if room[dx][dy] == 0:
            chk = True
            break

    if chk:
        if d == 0:
            for i in range(4):
                dx = x + dir0[i][0]
                dy = y + dir0[i][1]
                if room[dx][dy] == 0:
                    if i == 0:
                        k = 3
                    elif i == 1:
                        k = 2
                    elif i == 2:
                        k = 1
                    else:
                        k = 0
                    clean(dx, dy, k)
                    break
        elif d == 1:
            for i in range(4):
                dx = x + dir1[i][0]
                dy = y + dir1[i][1]
                if room[dx][dy] == 0:
                    if i == 0:
                        k = 0
                    elif i == 1:
                        k = 3
                    elif i == 2:
                        k = 2
                    else:
                        k = 1
                    clean(dx, dy, k)
                    break
        elif d == 2:
            for i in range(4):
                dx = x + dir2[i][0]
                dy = y + dir2[i][1]
                if room[dx][dy] == 0:
                    if i == 0:
                        k = 1
                    elif i == 1:
                        k = 0
                    elif i == 2:
                        k = 3
                    else:
                        k = 2
                    clean(dx, dy, k)
                    break
        else:
            for i in range(4):
                dx = x + dir3[i][0]
                dy = y + dir3[i][1]
                if room[dx][dy] == 0:
                    if i == 0:
                        k = 2
                    elif i == 1:
                        k = 1
                    elif i == 2:
                        k = 0
                    else:
                        k = 3
                    clean(dx, dy, k)
                    break
    if not chk:
        if d == 0:
            if room[x+1][y] != 1:
                clean(x+1, y, d)
        elif d == 1:
            if room[x][y-1] != 1:
                clean(x, y-1, d)
        elif d == 2:
            if room[x-1][y] != 1:
                clean(x-1, y, d)
        else:
            if room[x][y+1] != 1:
                clean(x, y+1, d)

clean(r, c, t)
print(cnt)