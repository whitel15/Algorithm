import sys
input = sys.stdin.readline

h, w = map(int, input().split())
input_strings = [input().strip() for _ in range(h)]
sky = [list(h) for h in input_strings]
a = 1
for i in range(h):
    for j in range(w):
        if sky[i][j] == 'c':
            sky[i][j] = 0


def cloud(x, y):
    global a
    if y < w and sky[x][y] != 0:
        sky[x][y] = a
        a += 1
        if y + 1 < w and sky[x][y + 1] != 0:
            cloud(x, y + 1)


for i in range(h):
    for j in range(w):
        if sky[i][j] == 0:
            a = 1
            cloud(i, j + 1)

for i in range(h):
    for j in range(w):
        if sky[i][j] == '.':
            sky[i][j] = -1

for i in range(h):
    for j in range(w):
        print(sky[i][j], end=" ")
    print()