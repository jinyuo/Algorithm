def solution(n):
    memo = [0, 1, 3]
    for i in range(3, int(n) + 1):
        memo.append(memo[i - 1] + 2 * memo[i - 2])
    return memo[n] % 10007


n = int(input())
print(solution(n))