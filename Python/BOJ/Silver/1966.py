import sys
input = sys.stdin.readline

k = int(input())
ans = []

for i in range(k):
    n, m = map(int, input().split())
    priority = list(map(int, input().strip().split()))
    text = []

    for j in range(n):
        text.append((priority[j], j))

    cnt = 1

    while len(text):
        sorted_text = sorted(text, key=lambda x: x[0], reverse=True)
        max = sorted_text[0][0]
        if text[0][0] == max:
            if text[0][1] == m:
                ans.append(cnt)
                break
            text.pop(0)
            cnt += 1
        else:
            t = text[0]
            text.pop(0)
            text.append(t)

for i in range(k):
    print(ans[i])