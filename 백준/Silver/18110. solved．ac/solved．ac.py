import sys

n = int(sys.stdin.readline())
grade = [int(sys.stdin.readline()) for _ in range(n)]
grade.sort()
withdraw_val = int(n * 0.15 + 0.5)
grade = grade[withdraw_val:n - withdraw_val]

print(0 if n == 0 else int((sum(grade) / (n - (withdraw_val * 2)) + 0.5)))