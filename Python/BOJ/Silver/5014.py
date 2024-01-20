from collections import deque
import sys
input = sys.stdin.readline

# F : 고층 건물의 층수
# S : 강호가 지금 있는 층수
# G : 스타트링크의 층수
# U : 위로 U층을 가는 버튼
# D : 아래로 D층을 가는 버튼

# U, D층 위나 D층 아래에 해당하는 층이 없을 때는 엘리베이터 움직이지 X
# 엘리베이터로 G층에 갈 수 없다면 use the stairs 출력

F, S, G, U, D = map(int, input().split())
ans = "use the stairs"
visited = [0 for _ in range(F+1)]

dq = deque()

dq.append((S, 0))
visited[S] = 1

while dq:
    floor, cnt = dq.popleft()
    if floor == G:
        ans = str(cnt)
        break
    if 0 < floor + U <= F and visited[floor + U] == 0:
        visited[floor + U] = 1
        dq.append((floor + U, cnt + 1))
    if 0 < floor - D <= F and visited[floor - D] == 0:
        visited[floor - D] = 1
        dq.append((floor - D, cnt + 1))

print(ans)