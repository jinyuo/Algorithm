import sys

n = int(sys.stdin.readline())
stack = []
target = [int(sys.stdin.readline()) for _ in range(n)]

val = 1
answer = []
while target:
    if stack and stack[-1] > n:
        break

    if stack and stack[-1] == target[0]:
        target.pop(0)
        stack.pop()
        answer.append('-')
    else:
        stack.append(val)
        val += 1
        answer.append('+')

print("\n".join(answer) if not stack else "NO")