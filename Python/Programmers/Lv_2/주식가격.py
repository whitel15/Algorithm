from collections import deque


def solution(prices):
    answer = []

    prices_deque = deque(prices)

    while prices_deque:
        a = prices_deque.popleft()
        tmp = len(prices_deque)
        answer.append(tmp)
        k = 0
        for i in prices_deque:
            k += 1
            if i < a:
                answer[-1] = k
                break

    return answer