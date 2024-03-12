import sys
t = int(sys.stdin.readline())
for i in range(1, t + 1):
    li = sorted(list(map(int, sys.stdin.readline().split())))
    print(f"Case #{i}:",
          ["invalid!", "scalene", "isosceles", "equilateral"][li.count(li[1]) if li[0] + li[1] > li[2] else 0])