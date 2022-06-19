import sys
def hanoi(n, from_p, to_p, aux_p):
    if n == 1:
        li.append((from_p, to_p))
        return
    hanoi(n - 1, from_p, aux_p, to_p)
    li.append((from_p, to_p))
    hanoi(n - 1, aux_p, to_p, from_p)


n = int(sys.stdin.readline())
li = []
hanoi(n, 1, 3, 2)
print(len(li))
for a, b in li:
    print(a, b)