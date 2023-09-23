def solution(elements):
    answer = []
    
    for i in range(len(elements)):
        s = 0
        for j in range(len(elements)):
            s += elements[(i+j) % len(elements)]
            answer.append(s)
    
    return len(set(answer))