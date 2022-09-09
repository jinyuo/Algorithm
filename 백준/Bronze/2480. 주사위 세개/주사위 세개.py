a, b, c = sorted(map(int, input().split()))
print([c, b + 10, b * 10 + 100][[a, b, c].count(b) - 1] * 100)