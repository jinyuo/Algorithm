loop = int(input())
score = 0
for i in range(loop):
    a, b, c = sorted(map(int, input().split()))
    tmp = [c, b + 10, b * 10 + 100][[a, b, c].count(b) - 1] * 100
    if tmp > score:
        score = tmp
print(score)