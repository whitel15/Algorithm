import sys
input = sys.stdin.readline

n = int(input())

score = {}
T1 = 0
T2 = 0
T1T = 0
T2T = 0

for i in range(n):
    a, b = input().strip().split(" ")
    m, s = b.split(":")
    score[int(m) * 60 + int(s)] = int(a)


for i in range(0, 48 * 60):
    if i in score:
        if score[i] == 1:
            T1 += 1
        else:
            T2 += 1

    if T1 > T2:
        T1T += 1
    elif T2 > T1:
        T2T += 1


def printT(time):
    m = str(time // 60)
    s = str(time % 60)
    if len(m) == 1:
        m = "0" + m
    if len(s) == 1:
        s = "0" + s
    return m + ":" + s

print(printT(T1T))
print(printT(T2T))