import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find_leaf(node):
    global answer, checked, delete_node

    if node == delete_node:
        return

    if len(graph[node]) == 0:
        answer += 1
        return

    for i in graph[node]:
        if checked[i]:
            continue

        checked[i] = True
        find_leaf(i)


N = int(input())

tree = list(map(int, input().strip().split()))

root = -1

graph = [[] for _ in range(N + 1)]
for node in range(N):
    p = tree[node]

    if p == -1:
        root = node
        continue

    graph[p].append(node)

delete_node = int(input())
graph[delete_node] = []

for g in graph:
    if delete_node in g:
        g.remove(delete_node)

checked = [False for _ in range(N)]
answer = 0

find_leaf(root)

print(answer)