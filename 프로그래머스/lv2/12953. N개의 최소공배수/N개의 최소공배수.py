def gcd(a, b):    
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def solution(arr):
    l = 1
    for i in range(len(arr)):
        l = lcm(l, arr[i])

    return l