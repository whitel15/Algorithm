def solution(cacheSize, cities):
    answer = 0
    cache = []

    if cacheSize == 0:
        return 5 * len(cities)

    for i in range(len(cities)):
        cities[i] = cities[i].upper()

    for i in range(len(cities)):
        if cities[i] in cache:
            answer += 1
            idx = cache.index(cities[i])
            cache = cache[:idx] + cache[idx + 1:]
            cache.append(cities[i])
        else:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(cities[i])
            else:
                cache = cache[1:]
                cache.append(cities[i])

    return answer