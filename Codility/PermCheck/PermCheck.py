# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter


def solution(A):
    # Implement your solution here
    counter_A = Counter(A)

    if any(i != 1 for i in counter_A.values()):
        return 0
    elif len(counter_A) == max(A):
        return 1
    else:
        return 0
