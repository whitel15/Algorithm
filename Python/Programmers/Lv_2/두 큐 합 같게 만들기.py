from collections import deque


def solution(queue1, queue2):
    answer = -1

    target = (sum(queue1) + sum(queue2)) / 2
    idx = len(queue1)
    cnt = 0

    dq = deque(queue1 + queue2)

    current_sum = sum(queue1)

    while idx not in [0, len(dq)] and cnt < len(queue1) * 8:
        if current_sum == target:
            return cnt
        elif current_sum > target:
            a = dq.popleft()
            current_sum -= a
            idx -= 1
        else:
            current_sum += dq[idx]
            idx += 1
        cnt += 1

    return answer
