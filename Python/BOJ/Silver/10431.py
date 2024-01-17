import sys
input = sys.stdin.readline

p = int(input())

for _ in range(p):
    line = list(map(int, input().split()))
    total = 0
    for i in range(1, len(line)-1):
        for j in range(i+1, len(line)):
            if line[i] > line[j]:
                line[i], line[j] = line[j], line[i]
                total += 1

    print(line[0], total)