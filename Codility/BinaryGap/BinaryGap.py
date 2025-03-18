# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    str_n = str(bin(N))[2:]
    list_idx = [i for i in range(len(str_n)) if str_n[i] == '1']
    if len(list_idx) <= 1:
        return 0
    else:
        gap = [list_idx[i + 1] - list_idx[i] - 1 for i in range(len(list_idx) - 1)]
        return max(gap)
