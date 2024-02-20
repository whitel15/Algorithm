import sys
input = sys.stdin.readline

gear = [list(input().strip()) for _ in range(4)]
k = int(input())
rotate = []
score = 0

for i in range(k):
    t, direction = map(int, input().split())
    rotate.append([t, direction])

for i in range(k):
    tr = []
    t, direction = rotate[i][0] - 1, rotate[i][1]
    tr.append([t, direction])

    left = t - 1
    DL = direction * -1
    right = t + 1
    DR = direction * -1

    while left >= 0:
        if gear[left + 1][6] != gear[left][2]:
            tr.append([left, DL])
            left -= 1
            DL *= -1
        else:
            break

    while right < 4:
        if gear[right - 1][2] != gear[right][6]:
            tr.append([right, DR])
            right += 1
            DR *= -1
        else:
            break

    for x, y in tr:
        if y == 1:
            gear[x] = [gear[x][7]] + gear[x][:7]
        else:
            gear[x] = gear[x][1:] + [gear[x][0]]

if gear[0][0] == "1":
    score += 1
if gear[1][0] == "1":
    score += 2
if gear[2][0] == "1":
    score += 4
if gear[3][0] == "1":
    score += 8

print(score)