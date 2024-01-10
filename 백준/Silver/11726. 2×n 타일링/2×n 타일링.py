def solution(n):
    memo = [0, 1, 2]
    for i in range(3, int(n) + 1):
        memo.append((memo[i - 1] + memo[i - 2]) % 10007)
    return memo[n]


n = int(input())
print(solution(n))