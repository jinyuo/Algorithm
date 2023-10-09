def union(a, b):
    result = a.copy()
    tmp = a.copy()
    
    for i in b:
        if i not in tmp:
            result.append(i)
        else:
            tmp.remove(i)
    return result


def intersection(a, b):
    result = []    
    for i in a:
        if i in b:
            b.remove(i)
            result.append(i)
    return result


def solution(str1, str2):
    MUL_VAL = 65536
    set1 = [str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    set2 = [str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]
    set_uni = union(set1, set2)
    set_int = intersection(set1, set2)
    
    if not (set_uni or set_int):
        return 1 * MUL_VAL
    return int(len(set_int) / len(set_uni) * MUL_VAL)