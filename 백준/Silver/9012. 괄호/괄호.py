import sys


def check_ps(ps):
    stack = []
    for p in ps:
        if p == "(":
            stack.append(p)
        elif p == ")":
            try:
                stack.pop()
            except:
                return False
    return False if stack else True


T = int(sys.stdin.readline())
for _ in range(T):
    ps = list(sys.stdin.readline())
    stack = []
    print("YES" if check_ps(ps) else "NO")