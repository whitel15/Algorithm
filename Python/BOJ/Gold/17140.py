import sys
input = sys.stdin.readline
from collections import Counter

r, c, k = map(int, input().split())
A = []
for i in range(3):
    A.append(list(map(int, input().split())))
cnt = 0
chk = 1


def cal(matrix, dir):
    global A
    size = 0
    new_list = []

    for i in range(len(matrix)):
        line = []
        for key, value in Counter(matrix[i]).items():
            if key != 0:
                line.append([key, value])

        line.sort(key=lambda x: (x[1], x[0]))

        sorted_line = []
        for j in range(len(line)):
            for z in range(len(line[0])):
                sorted_line.append(line[j][z])
        new_list.append(sorted_line)

    for i in range(len(new_list)):
        size = max(size, len(new_list[i]))
        if len(new_list[i]) > 100:
            size = 100
            break

    for i in range(len(new_list)):
        if len(new_list[i]) < size:
            new_list[i] += [0 for _ in range(size - len(new_list[i]))]
        elif len(new_list[i]) > 100:
            new_list[i] = new_list[i][:size]

    if dir == "R":
        A = new_list
    else:
        A = list(zip(*new_list))


while cnt <= 100:
    if len(A) >= r and len(A[r-1]) >= c and A[r-1][c-1] == k:
        print(cnt)
        chk = 0
        break

    if len(A) >= len(A[0]):
        cal(A, "R")
    else:
        cal(list(zip(*A)), "C")

    cnt += 1

if chk:
   print(-1)
