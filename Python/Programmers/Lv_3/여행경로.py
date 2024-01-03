from collections import deque


def solution(tickets):
    answer = []

    tickets.sort(key=lambda x: (x[0], x[1]))

    dq = deque([(["ICN"], tickets)])

    while dq:
        path, left_ticket = dq.popleft()

        if len(left_ticket) == 0:
            answer = path
            break

        idx = -1
        for i in range(len(left_ticket)):
            if left_ticket[i][0] == path[-1]:
                idx = i
                break

        if idx == -1:
            continue

        while idx < len(left_ticket) and left_ticket[idx][0] == path[-1]:
            dq.append((path + [left_ticket[idx][1]], left_ticket[:idx] + left_ticket[idx + 1:]))
            idx += 1

    return answer