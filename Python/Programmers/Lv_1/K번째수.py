def solution(array, commands):
    answer = []
    buck = []

    for x in range(len(commands)):
        i = commands[x][0]
        j = commands[x][1]
        k = commands[x][2]
        for y in range(i - 1, j):
            buck.append(array[y])
        buck.sort()
        answer.append(buck[k - 1])
        buck = []

    return answer