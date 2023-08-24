def solution(s):
    stack = []
    
    for t in s:
        if stack:
            if stack[-1] == t:
                stack.pop()
            else:
                stack.append(t)
        else:
            stack.append(t)
        
    return 0 if stack else 1