# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    if not A:
        return 1

    set_total = set(range(1, max(A) + 2))
    set_diff = set_total - set(A)

    return min(set_diff)
