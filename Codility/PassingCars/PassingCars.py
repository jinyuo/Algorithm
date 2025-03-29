# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    result = 0
    east = 0
    for a in A:
        if a == 0:
            east += 1
        elif a == 1:
            result += east

        if result > 1000000000:
            return -1
    return result
