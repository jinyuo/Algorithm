def solution(keymap, targets):
    answer = []
    key_map = dict()
    for key in keymap:
        for i in range(len(key)):
            if key[i] not in key_map.keys():
                key_map[key[i]] = i
            else:
                if i < key_map[key[i]]:
                    key_map[key[i]] = i
    
    for target in targets:
        try:
            answer.append(sum([key_map[t] + 1 for t in target]))
        except KeyError:
            answer.append(-1)
    
    return answer