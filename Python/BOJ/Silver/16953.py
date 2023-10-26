from collections import deque

n, m = map(int, input().split())


def bfs(first, last):
    queue = deque()
    queue.append(last)
    cnt = 1
    var = last
    while var >= first:
        x = queue.popleft()
        if x == first:
            return cnt
        elif x % 2 == 0:
            x //= 2
            cnt += 1
            queue.append(x)
            var = x
        elif (x // 10) * 10 + 1 == x:
            x //= 10
            cnt += 1
            queue.append(x)
            var = x
        else:
            return -1

    return -1


print(bfs(n, m))
