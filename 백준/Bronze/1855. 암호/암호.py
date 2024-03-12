import sys

k = int(sys.stdin.readline())
enco = sys.stdin.readline()[:-1]
li = [enco[i:i+k] for i in range(0, len(enco), k)]
for i in range(len(li)):
    if i % 2 == 1:
        li[i] = li[i][::-1]
li = [l[j] for j in range(k) for l in li]
print("".join(li))