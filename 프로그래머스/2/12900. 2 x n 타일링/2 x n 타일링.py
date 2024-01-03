memo = [0, 1]

def fib(n):
    l = len(memo)
    if l < n:
        for i in range(l, n):
            memo.append((memo[i - 1] + memo[i - 2]) % 1000000007)
    return memo[n - 1]

def solution(n):
    return fib(n + 2)