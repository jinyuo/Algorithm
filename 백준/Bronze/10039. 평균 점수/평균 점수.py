import sys
sum_s = 0
for i in range(5):
    n = int(sys.stdin.readline());
    n = 40 if n < 40 else n
    sum_s += n
print(sum_s // 5)