import sys
input = sys.stdin.readline

n = int(input())
num = []
num.append(-1)
cnt = 0
ans = []
same = []

for i in range(n):
    num.append(int(input()))

for i in range(1, n+1):
    if i == num[i]:
        same.append(i)


def dfs(x):
    visited[x] = 1
    if visited[num[x]] == 0:
        dfs(num[x])


for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    idx = []
    element = []
    dfs(i)
    for j in range(1, n+1):
        if visited[j] == 1:
            idx.append(j)
            element.append(num[j])
    set1 = set(idx)
    set2 = set(element)
    if set1 == set2:
        for k in same:
            if k not in idx:
                idx.append(k)
        ans.append(idx)

ne = []
for i in range(len(ans)):
    for j in range(len(ans[i])):
        if ans[i][j] not in ne:
            ne.append(ans[i][j])

ne.sort()

print(len(ne))
for i in ne:
    print(i)