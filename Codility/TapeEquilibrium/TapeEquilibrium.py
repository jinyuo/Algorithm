# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    first_part = A[0]
    second_part = sum(A) - first_part
    min_gap = abs(first_part - second_part)
    for a in A[1:-1]:
        first_part += a
        second_part -= a
        min_gap = min(min_gap, abs(first_part - second_part))

    return min_gap
