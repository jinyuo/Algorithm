import sys
n = int(sys.stdin.readline())
rank = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
rank.sort(key=lambda x: x[2], reverse=True)
award = list()
for r in rank:
    if len(award) == 3:
        break
    if [c[0] for c in award].count(r[0]) < 2:
        award.append(r[:2])
for a in award:
    print(*a)