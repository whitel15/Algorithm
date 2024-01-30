import sys
input = sys.stdin.readline

room = []
players = []

p, m = map(int, input().split())

for i in range(p):
    l, n = input().rstrip().split(" ")
    players.append([int(l), n])

for i in range(p):
    if len(room) == 0:
        room.append([players[i]])
    else:
        a = True
        for j in range(len(room)):
            if room[j][0][0] - 10 <= players[i][0] <= room[j][0][0] + 10 and len(room[j]) < m:
                room[j].append(players[i])
                a = False
                break
        if a:
            room.append([players[i]])

for i in range(len(room)):
    if len(room[i]) != m:
        print("Waiting!")
        s = sorted(room[i], key=lambda x: x[1])
        for k in range(len(room[i])):
            print(s[k][0], s[k][1])
    else:
        print("Started!")
        s = sorted(room[i], key=lambda x: x[1])
        for k in range(m):
            print(s[k][0], s[k][1])
