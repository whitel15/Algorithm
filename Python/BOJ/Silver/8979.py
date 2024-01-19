import sys
input = sys.stdin.readline

n, k = map(int, input().split())
medal = []

for i in range(n):
    nation, gold, silver, bronze = map(int, input().split())
    medal.append([nation, gold, silver, bronze])

sorted_medal = sorted(medal, key=lambda x: (x[1], x[2], x[3]), reverse=True)

rank = 1
duplication = 0

for i in range(n):
    if sorted_medal[i][0] == k:
        print(rank)
        break
    if sorted_medal[i][1] == sorted_medal[i+1][1]:
        if sorted_medal[i][2] == sorted_medal[i+1][2]:
            if sorted_medal[i][3] == sorted_medal[i + 1][3]:
                duplication += 1
            else:
                rank += (duplication + 1)
                duplication = 0
        else:
            rank += (duplication + 1)
            duplication = 0
    else:
        rank += (duplication + 1)
        duplication = 0
