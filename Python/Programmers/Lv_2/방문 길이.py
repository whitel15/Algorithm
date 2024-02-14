def solution(dirs):
    visited = set()
    d = {'U' : (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x = 0
    y = 0

    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            x, y = nx, ny

    return len(visited) // 2