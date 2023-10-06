from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    for c in cities:
        c = c.lower() 
        if c in cache:
            cache.remove(c)
            answer += 1
        else:
            answer += 5
        cache.append(c)
    return answer