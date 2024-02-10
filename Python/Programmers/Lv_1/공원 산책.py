def solution(park, routes):
    answer = []
    x = 0
    y = 0

    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                x = i
                y = j
                break

    for i in range(len(routes)):
        op, cnt = routes[i].split()
        cnt = int(cnt)
        a = 1
        if op == "E":
            if y + cnt < len(park[0]):
                for j in range(y, y + cnt + 1):
                    if park[x][j] == "X":
                        a = 0
                        break
                if a:
                    y = y + cnt
        elif op == "W":
            if y - cnt >= 0:
                for j in range(y - cnt, y):
                    if park[x][j] == "X":
                        a = 0
                        break
                if a:
                    y = y - cnt
        elif op == "N":
            if x - cnt >= 0:
                for j in range(x - cnt, x):
                    if park[j][y] == "X":
                        a = 0
                        break
                if a:
                    x = x - cnt
        elif op == "S":
            if x + cnt < len(park):
                for j in range(x, x + cnt + 1):
                    if park[j][y] == "X":
                        a = 0
                        break
                if a:
                    x = x + cnt

    answer.append(x)
    answer.append(y)

    return answer