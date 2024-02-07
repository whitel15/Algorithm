def solution(bandage, health, attacks):
    idx = 0
    Hidx = 0
    M = health

    for i in range(attacks[-1][0] + 1):

        if idx < len(attacks) and i == attacks[idx][0]:
            health -= attacks[idx][1]
            if health <= 0:
                return -1
            idx += 1
            Hidx = 0

        else:
            health += bandage[1]
            if health > M:
                health = M
            Hidx += 1
            if Hidx == bandage[0]:
                health += bandage[2]
                Hidx = 0
                if health > M:
                    health = M

    return health