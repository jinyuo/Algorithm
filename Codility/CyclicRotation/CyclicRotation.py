# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here
    if not A:
        return A

    arr_A = 2 * A
    length = len(A)
    start_idx = length - (K % length)
    
    return arr_A[start_idx:start_idx + length]
