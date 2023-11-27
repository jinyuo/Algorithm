def solution(n, m, section):
    answer = 0
    now_section = 0
    for s in section:
        if now_section < s:
            now_section = s + m - 1
            answer += 1          
            
    return answer