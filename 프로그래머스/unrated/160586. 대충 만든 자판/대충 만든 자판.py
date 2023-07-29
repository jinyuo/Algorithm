def solution(keymap, targets):
    key_map = dict()
    for key in keymap:
        for i in range(len(key)):
            key_map[key[i]] = min(key_map[key[i]], i) if key[i] in key_map.keys() else i

    answer = []
    for target in targets:
        try:
            answer.append(sum([key_map[t] + 1 for t in target]))
        except KeyError:
            answer.append(-1)
    
    return answer