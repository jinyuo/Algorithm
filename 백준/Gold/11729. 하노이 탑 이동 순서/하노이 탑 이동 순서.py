import sys
def hanoi(n, from_p, to_p, aux_p):
    if n == 1:
        print(from_p, to_p)
        return
    hanoi(n - 1, from_p, aux_p, to_p)
    print(from_p, to_p)
    hanoi(n - 1, aux_p, to_p, from_p)


n = int(sys.stdin.readline())
print(2 ** n - 1)
hanoi(n, 1, 3, 2)