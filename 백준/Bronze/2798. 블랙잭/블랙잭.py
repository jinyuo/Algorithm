import sys
n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
card.sort(reverse=True)
s = set()
l = len(card)
for i in range(l - 2):
    if card[i] > m:
        continue
    for j in range(i + 1, l - 1):
        if card[i] + card[j] > m:
            continue
        for k in range(j + 1, len(card)):
            if card[i] + card[j] + card[k] <= m:
                s.add(card[i] + card[j] + card[k])
print(max(s))

