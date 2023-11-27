def check(bracket):
    stack = []
    for b in bracket:
        if stack:
            if b == ')' and stack[-1] == '(':
                stack.pop()
            elif b == '}' and stack[-1] == '{':
                stack.pop()
            elif b == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(b)
        else:
            stack.append(b)
    return not stack


def solution(s):
    answer = 0
    len_s = len(s)
    s += s

    for i in range(len_s):
        tmp = s[i:i+len_s]
        if check(tmp):
            answer += 1

    return answer

