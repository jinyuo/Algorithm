# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    max_A = max(A)
    if max_A < 0:
        return 1

    total_A = set(range(1, max_A + 2))
    return min(total_A - set(A))
