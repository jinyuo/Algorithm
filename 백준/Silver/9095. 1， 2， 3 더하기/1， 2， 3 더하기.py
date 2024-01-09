def solution(n):
    memo = [0, 1, 2, 4]
    for i in range(4, int(n) + 1):
        memo.append(memo[i - 1] + memo[i - 2] + memo[i - 3])
    return memo[n]


T = int(input())
for i in range(T):
    n = int(input())
    print(solution(n))