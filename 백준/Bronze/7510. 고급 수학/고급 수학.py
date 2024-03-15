import sys
for i in range(int(sys.stdin.readline())):
    li = sorted(map(int, sys.stdin.readline().split()))
    print(f"Scenario #{i + 1}:\n{'yes' if li[0]**2 + li[1]**2 == li[2]**2 else 'no'}\n")
