def solution(skill, skill_trees):
    answer = 0

    v = [i for i in range(len(skill))]

    for i in range(len(skill_trees)):
        chk = []
        a = 1
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                chk.append(skill.index(skill_trees[i][j]))

        for j in range(len(chk)):
            if j != chk[j]:
                a = 0
                break
        if a:
            answer += 1

    return answer