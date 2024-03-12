import sys
a, b, c = map(int, sys.stdin.readline().split())
oper = "+/*-"
for i in oper:
    if eval(f"{a}{i}{b}=={c}"):
        print(f"{a}{i}{b}={c}")
        exit()
    elif eval(f"{a}=={b}{i}{c}"):
        print(f"{a}={b}{i}{c}")
        exit()