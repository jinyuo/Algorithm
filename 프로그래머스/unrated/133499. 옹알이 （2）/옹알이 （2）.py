def solution(babbling):
    defi = ["aya", "ye", "woo", "ma"]
    answer = 0
    for b in babbling:
        for d in defi:
            if d * 2 not in b:
                b = b.replace(d, ' ')
        b = b.replace(' ', '')
        if not b:
            answer += 1
    
    return answer