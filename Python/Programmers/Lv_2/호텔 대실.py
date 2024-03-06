def solution(book_time):
    answer = 0
    book_time.sort(key=lambda x: (x[0], x[1]))
    sim = []

    for time in book_time:
        s1, s2 = time[0].split(":")
        s = int(s1) * 60 + int(s2)
        e1, e2 = time[1].split(":")
        e = int(e1) * 60 + int(e2) + 10

        if len(sim) == 0:
            sim.append(e)
        else:
            if s >= sim[-1]:
                while len(sim) > 0 and s >= sim[-1]:
                    sim.pop()
                sim.append(e)
            else:
                sim.append(e)

        answer = max(answer, len(sim))
        sim.sort(reverse=True)

    return answer