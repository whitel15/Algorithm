from itertools import permutations


def solution(k, dungeons):
    answer = -1

    idx = [i for i in range(len(dungeons))]

    new_idx = list(permutations(idx, len(idx)))

    for i in range(len(new_idx)):
        result = 0
        now = k
        for j in new_idx[i]:
            if now >= dungeons[j][0]:
                now -= dungeons[j][1]
                result += 1
        if result > answer:
            answer = result

    return answer