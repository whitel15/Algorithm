def solution(str1, str2):
    answer = 0

    s1 = [str1[n:n + 2].lower() for n in range(len(str1) - 1) if str1[n:n + 2].isalpha()]
    s2 = [str2[n:n + 2].lower() for n in range(len(str2) - 1) if str2[n:n + 2].isalpha()]

    s12 = set(s1) | set(s2)
    union = 0
    intersection = 0

    if s12:
        for i in s12:
            union += max(s1.count(i), s2.count(i))
            intersection += min(s1.count(i), s2.count(i))

        print(union, intersection)
        return int(intersection / union * 65536)

    else:
        return 65536