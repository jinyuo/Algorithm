import sys
t = int(sys.stdin.readline())
for i in range(1, t+1):
    print(f"Case {i}: {['NO','YES'][eval(sys.stdin.readline()[:-1].replace('=', '=='))]}")