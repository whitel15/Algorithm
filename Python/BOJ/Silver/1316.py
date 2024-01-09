import sys
input = sys.stdin.readline

n = int(input())
word = []
check = [[] for _ in range(26)]
ans = n

for i in range(n):
    word.append(input().strip())

for i in range(len(word)):
    gw = word[i]
    for j in range(len(gw)):
        check[ord(gw[j]) - ord('a')].append(j)
    checker = 0
    for j in range(len(check)):
        if len(check[j]) > 1:
            for k in range(len(check[j])-1):
                if check[j][k+1] - check[j][k] > 1:
                    checker = 1
                    break
    ans -= checker
    check = [[] for _ in range(26)]

print(ans)