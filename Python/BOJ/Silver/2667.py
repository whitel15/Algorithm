n = int(input())
list = [[] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
ans = [[] for _ in range(n*n)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(x, y, counter):
    visited[x][y] = 1
    for i in range(4):
        dx = x + direction[i][0]
        dy = y + direction[i][1]
        if 0 <= dx < n and 0 <= dy < n and visited[dx][dy] == 0 and list[dx][dy] == 1:
            counter[0] += 1
            dfs(dx, dy, counter)


for i in range(n):
    line = input()
    for j in line:
        list[i].append(int(j))

cnt = 0
for i in range(n):
    for j in range(n):
        if list[i][j] == 1 and visited[i][j] == 0:
            count = [1]
            dfs(i, j, count)
            ans[cnt].append(count[0])
            cnt += 1

print(cnt)

sorted_ans = []
for i in range(cnt):
    sorted_ans.append(ans[i][0])

sorted_ans.sort()

for i in sorted_ans:
    print(i)
