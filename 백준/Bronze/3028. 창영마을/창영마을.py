import sys
li = [1, 0, 0]
sw = sys.stdin.readline()[:-1]
for s in sw:
    if s == "A":
        li[0], li[1] = li[1], li[0]
    elif s == "B":
        li[1], li[2] = li[2], li[1]
    else:
        li[0], li[2] = li[2], li[0]
print(li.index(1) + 1)