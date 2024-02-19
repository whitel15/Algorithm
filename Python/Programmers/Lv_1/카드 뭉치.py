def solution(cards1, cards2, goal):
    a, b, c = 0, 0, 0

    while True:
        if c == len(goal):
            return "Yes"
        if a < len(cards1) and goal[c] == cards1[a]:
            c += 1
            a += 1
        elif b < len(cards2) and goal[c] == cards2[b]:
            c += 1
            b += 1
        else:
            return "No"