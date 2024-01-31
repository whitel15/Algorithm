import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))

Nline = [0 for _ in range(n)]

for i in range(n):
    cnt = 0
    if line[i] == 0:
        for m in range(n):
            if Nline[m] == 0:
                Nline[m] = i + 1
                break
    else:
        for j in range(n):
            if Nline[j] == 0:
                cnt += 1
            if cnt == line[i]:
                for m in range(j + 1, n):
                    if Nline[m] == 0:
                        Nline[m] = i + 1
                        break
                break

for i in Nline:
    print(i, end=" ")