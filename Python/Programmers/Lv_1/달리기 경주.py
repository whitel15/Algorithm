def solution(players, callings):
    name = {}

    for i in range(len(players)):
        name[players[i]] = i

    for i in callings:
        idx = name[i]

        name[i] -= 1
        name[players[idx - 1]] += 1

        players[idx - 1], players[idx] = i, players[idx - 1]

    return players