import sys
i = 1
while True:
    e = sys.stdin.readline()
    if e.find("E") > -1:
        exit()
    print(f"Case {i}: {str(eval(e)).lower()}")
    i += 1
