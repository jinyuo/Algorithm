from collections import Counter
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    counter_A = Counter(A)

    for k, v in counter_A.items():
        if v % 2 != 0:
            return k
