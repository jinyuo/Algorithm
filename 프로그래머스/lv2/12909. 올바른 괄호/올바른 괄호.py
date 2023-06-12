def solution(str_val):
    stack = []
    for s in str_val:
        if s == '(':
            stack.append(s)
        elif s == ')' :
            try:
                stack.pop()
            except:
                return False
            
    return not stack
    