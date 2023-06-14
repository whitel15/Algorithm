import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m, v = map(int, input().split())
list = [[] for _ in range(n+1)]
check = [False] * (n + 1)
check2 = [False] * (n + 1)
DFS = []
BFS = []
ans = []

for i in range(m):
    a, b = map(int, input().split())
    list[a].append(b)
    list[b].append(a)

for i in range(n):
    list[i+1].sort()


def Dsort(a):
    check[a] = True
    DFS.append(a)
    for i in list[a]:
        if not check[i]:
            Dsort(i)


Dsort(v)

for i in range(len(DFS)):
    print(DFS[i], end=" ")


def Bsort(a):
    check2[a] = True
    ans.append(a)
    for i in list[a]:
        if not check2[i]:
            BFS.append(i)
            check2[i] = True
    if BFS:
        Bsort(BFS.pop(0))

Bsort(v)
print()
for i in range(len(ans)):
    print(ans[i], end=" ")
