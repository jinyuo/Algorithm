def solution(babbling):
    answer = 0
    for b in babbling:
        for d in ["aya", "ye", "woo", "ma"]:
            if d * 2 not in b:
                b = b.replace(d, ' ')
        b = b.replace(' ', '')
        if not b:
            answer += 1
    
    return answer