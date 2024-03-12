import sys
for i in '_' * int(sys.stdin.readline()):
    print(len(set(sys.stdin.readline()[:-1])))