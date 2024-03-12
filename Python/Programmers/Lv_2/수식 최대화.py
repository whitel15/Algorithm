from itertools import permutations
from collections import deque
import copy

def solution(expression):
    answer = 0
    op = []
    a = ""
    dq = deque()
    q = deque()

    for i in range(len(expression)):
        if expression[i] not in ["*", "+", "-"]:
            a += expression[i]
        else:
            q.append(int(a))
            q.append(expression[i])
            a = ""
        if i == len(expression) - 1:
            q.append(int(a))

    for i in ["*", "+", "-"]:
        if i in expression:
            op.append(i)

    nq = copy.deepcopy(q)

    for i in list(permutations(op, len(op))):
        for j in i:
            while nq:
                now = nq.popleft()

                if now == j:
                    if j == "*":
                        dq.append(dq.pop() * nq.popleft())
                    elif j == "+":
                        dq.append(dq.pop() + nq.popleft())
                    else:
                        dq.append(dq.pop() - nq.popleft())

                else:
                    dq.append(now)
            nq = dq
            dq = deque()

        answer = max(answer, abs(nq.pop()))
        nq = copy.deepcopy(q)

    return answer