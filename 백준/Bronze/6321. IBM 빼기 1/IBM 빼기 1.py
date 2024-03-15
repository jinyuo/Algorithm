import sys
n = int(sys.stdin.readline())
for i in range(n):
    com = sys.stdin.readline()[:-1]
    t = ""
    for c in com:
        t += chr(ord(c) + 1) if c != "Z" else "A"
    print(f"String #{i+1}\n{t}\n")
