def solution(k, tangerine):
    t_group = dict()

    for i in tangerine:
        if i in t_group:
            t_group[i] += 1
        else:
            t_group[i] = 1
    t_group = sorted(t_group.items(), key=lambda x: x[1], reverse=True)
    
    answer = 0
    cnt = 0
    for g, c in t_group:
        if cnt < k:
            cnt += c
            answer += 1
    
    return answer