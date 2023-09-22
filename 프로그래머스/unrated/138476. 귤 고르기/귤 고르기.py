from collections import Counter

def solution(k, tangerine):
    t_group = Counter(tangerine)
    answer = 0
    cnt = 0
    for c in sorted(t_group.values(), reverse=True):
        if cnt < k:
            cnt += c
            answer += 1
    return answer