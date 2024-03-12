import sys

l = [int(sys.stdin.readline()) for _ in range(10)]
freq = {x: l.count(x) for x in set(l)}

print(sum(l) // len(l))
print(next(x for x in freq.keys() if freq[x] == max(freq.values())))