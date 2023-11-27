def solution(nums):
    answer = 0
    dic = {}

    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    if len(dic) > len(nums) // 2:
        answer = len(nums) // 2
    else:
        answer = len(dic)

    return answer