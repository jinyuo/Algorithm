import sys

N = int(sys.stdin.readline())
list_users = [sys.stdin.readline().split() for _ in range(N)]
list_users = [(int(age), name) for age, name in list_users]
list_users.sort(key=lambda x: x[0])
print("\n".join([f"{age} {name}" for age, name in list_users]))