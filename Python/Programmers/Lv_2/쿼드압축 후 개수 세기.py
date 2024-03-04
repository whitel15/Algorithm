def solution(arr):
    answer = [0, 0]

    line = len(arr)

    def check(x, y, length):
        same = arr[x][y]
        for i in range(x, x + length):
            for j in range(y, y + length):
                if arr[i][j] != same:
                    new_length = length // 2
                    for dx, dy in [(x, y), (x, y + new_length), (x + new_length, y), (x + new_length, y + new_length)]:
                        check(dx, dy, new_length)
                    return
        answer[same] += 1

    check(0, 0, line)

    return answer