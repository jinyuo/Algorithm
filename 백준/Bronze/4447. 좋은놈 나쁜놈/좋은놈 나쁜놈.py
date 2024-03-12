import sys
n = int(sys.stdin.readline())
for _ in range(n):
    name = sys.stdin.readline()[:-1]
    g = name.lower().count('g')
    b = name.lower().count("b")
    print(f"{name} is {'NEUTRAL' if g == b else ('GOOD' if g > b else 'A BADDY')}")
