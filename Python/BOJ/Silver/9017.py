from collections import Counter
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    chart = list(map(int, input().strip().split()))
    counter = Counter(chart)
    dic = {}

    tmp = 0
    for i in range(n):
        if counter[chart[i]] < 6:
            tmp += 1
            continue
        if chart[i] in dic:
            dic[chart[i]].append(i - tmp)
        else:
            dic[chart[i]] = [i - tmp]

    print(sorted(dic, key= lambda x:(sum(dic[x][0:4]), dic[x][4]))[0])

