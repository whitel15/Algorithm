import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while len(scoville) > 1:
        a = heapq.heappop(scoville)

        if a >= K:
            return answer
        else:
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a + b * 2)
            answer += 1

    if len(scoville) == 1:
        if heapq.heappop(scoville) >= K:
            return answer
        else:
            return -1