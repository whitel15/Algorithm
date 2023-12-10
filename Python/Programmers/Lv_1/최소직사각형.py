def solution(sizes):
    w = 0
    h = 0

    for i, j in sizes:
        if i > w:
            w = i
        if j > w:
            w = j

    for i, j in sizes:
        m = min(i, j)
        if m > h:
            h = m

    return w * h