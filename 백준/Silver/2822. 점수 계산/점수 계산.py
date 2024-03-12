import sys
score = [int(sys.stdin.readline()) for _ in range(8)]
result = sorted(score)[3:]
print(sum(result))
print(" ".join([str(i + 1) for i in range(len(score)) if score[i] in result]))