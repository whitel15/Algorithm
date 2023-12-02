from collections import deque

def solution(progresses, speeds):
    bp = []
    answer = []
    x = 0
    count = 0

    for i in range(len(progresses)):
        bp.append(((100 - progresses[i]) // speeds[i]) + (((100 - progresses[i]) % speeds[i]) > 0))

    bp = deque(bp)

    while bp:
        front = bp.popleft()
        count = 1
        while bp and front >= bp[0]:
            bp.popleft()
            count += 1

        answer.append(count)

    return answer