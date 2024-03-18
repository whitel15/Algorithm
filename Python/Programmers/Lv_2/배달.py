import heapq

def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    distance = [INF] * (N + 1)
    v = [[] for _ in range(N + 1)]

    for i in road:
        a, b, c = i[0], i[1], i[2]
        v[a].append((b, c))
        v[b].append((a, c))

    q = []
    heapq.heappush(q, (1, 0))
    distance[1] = 0

    while q:
        node, dis = heapq.heappop(q)

        if dis > distance[node]:
            continue

        for i in v[node]:
            if dis + i[1] < distance[i[0]]:
                distance[i[0]] = dis + i[1]
                heapq.heappush(q, (i[0], dis + i[1]))

    for i in distance:
        if i <= K:
            answer += 1

    return answer