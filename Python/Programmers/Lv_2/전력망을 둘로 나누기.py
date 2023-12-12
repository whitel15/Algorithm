def bfs(graph, start_node):
    visit = [start_node]
    queue = [start_node]

    while queue:
        node = queue.pop(0)
        for i in graph[node]:
            if i not in visit:
                visit.append(i)
                queue.append(i)

    return len(visit)


def solution(n, wires):
    answer = n

    for i in range(n - 1):
        a = [[] for _ in range(n+1)]

        for x, y in wires[:i] + wires[i+1:]:
            a[x].append(y)
            a[y].append(x)

        first = bfs(a, 1)
        second = n - first

        if abs(first - second) < answer:
            answer = abs(first - second)

    return answer