from collections import Counter

def solution(topping):
    answer = 0
    
    a = set()
    b = Counter(topping)
    for t in topping:
        a.add(t)
        b[t] -= 1
        
        if b[t] == 0:
            b.pop(t)
        
        if len(a) == len(b):
            answer += 1

    return answer