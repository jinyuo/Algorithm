import sys

X, Y = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
list_price = [map(int, sys.stdin.readline().split()) for _ in range(N)]
list_price.append((X, Y))
list_calc = [round(1000 / y * x, 2) for x, y in list_price]
print(f"{min(list_calc):.2f}")