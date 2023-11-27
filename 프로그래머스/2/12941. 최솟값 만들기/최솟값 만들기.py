def solution(A,B):
    A = sorted(A)
    B = sorted(B, reverse=True)
    return min(sum(A[i] * B[i] for i in range(len(A))), sum(A[i] * B[i] for i in range(len(A) - 1, -1, -1)))