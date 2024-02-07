def solution(edges):
    answer = [0, 0, 0, 0]
    m = 0
    graph = {}

    for i in range(len(edges)):
        m = max(m, edges[i][0], edges[i][1])

    for i in range(1, m + 1):
        # in, out
        graph[i] = [0, 0]

    for i in range(len(edges)):
        graph[edges[i][0]][1] += 1
        graph[edges[i][1]][0] += 1

    for i in range(1, len(graph) + 1):
        if graph[i][1] == 0:
            answer[2] += 1
        elif graph[i][1] == 1:
            continue
        elif graph[i][1] == 2:
            if graph[i][0] >= 2:
                answer[3] += 1
            else:
                answer[0] = i
        else:
            answer[0] = i

    answer[1] = graph[answer[0]][1] - answer[2] - answer[3]

    return answer