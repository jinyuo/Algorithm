def solution(keymap, targets):
    key_cnt = dict()
    for key in keymap:
        for i in range(len(key)):
            key_cnt[key[i]] = min(key_cnt[key[i]], i) if key[i] in key_cnt.keys() else i

    answer = []
    for target in targets:
        try:
            answer.append(sum([key_cnt[t] + 1 for t in target]))
        except KeyError:
            answer.append(-1)
    
    return answer