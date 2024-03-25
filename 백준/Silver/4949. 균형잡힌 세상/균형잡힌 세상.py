import sys


def check_braket(str_input):
    stack = []
    for s in str_input:
        try:
            if s in ['(', '[']:
                stack.append(s)
            elif (s == ')' and stack.pop() != '(') or (s == ']' and stack.pop() != '['):
                return False
        except IndexError:
            return False
    return stack == []


while True:
    str_input = sys.stdin.readline().rstrip()
    if str_input == '.':
        quit()
    print('yes' if check_braket(str_input) else 'no')