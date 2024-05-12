import sys

N, M = map(int, sys.stdin.readline().split())
A = [int(sys.stdin.readline()) for _ in range(N)]
for i in range(1, M + 1):
    for j in range(N - 1):
        if (A[j] % i) > A[j + 1] % i:
            A[j], A[j + 1] = A[j + 1], A[j]

print("\n".join(str(i) for i in A))