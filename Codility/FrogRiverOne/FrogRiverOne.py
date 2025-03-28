# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    d = dict()

    for i, a in enumerate(A):
        if a not in d.keys():
            d[a] = i
        
        if len(d.keys()) == X:
            return i
        
    return -1
