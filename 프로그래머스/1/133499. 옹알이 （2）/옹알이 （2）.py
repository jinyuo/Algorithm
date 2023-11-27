def solution(babbling):
    answer = 0
    for b in babbling:
        for d in ["aya", "ye", "woo", "ma"]:
            if d * 2 not in b:
                b = b.replace(d, ' ')
        if not b.strip():
            answer += 1
    
    return answer