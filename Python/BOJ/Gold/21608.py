import sys
input = sys.stdin.readline

n = int(input())
seat = {}
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
fs = [[-1 for _ in range(n)] for _ in range(n)]

for i in range(n**2):
    line = list(map(int, input().split()))
    seat[line[0]] = line[1:]

for student, like in seat.items():
    hts = []
    for j in range(n):
        for z in range(n):
            if fs[j][z] == -1:
                a, b = 0, 0
                for k in range(4):
                    dx = j + move[k][0]
                    dy = z + move[k][1]
                    if 0 <= dx < n and 0 <= dy < n:
                        if fs[dx][dy] in like:
                            a += 1
                        elif fs[dx][dy] == -1:
                            b += 1
                hts.append([a, b, j, z])
    hts.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    fs[hts[0][2]][hts[0][3]] = student

result = 0
point = [0, 1, 10, 100, 1000]

for i in range(n):
    for j in range(n):
        cnt = 0
        for z in range(4):
            dx = i + move[z][0]
            dy = j + move[z][1]
            if 0 <= dx < n and 0 <= dy < n:
                if fs[dx][dy] in seat[fs[i][j]]:
                    cnt += 1
        result += point[cnt]

print(result)
