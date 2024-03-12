import sys
n = int(sys.stdin.readline())
r = []
card = [i for i in range(1, n + 1)]
while len(card) > 1:
    r.append(card.pop(0))
    card.append(card.pop(0))
r.append(card.pop())
print(" ".join(str(i) for i in r))