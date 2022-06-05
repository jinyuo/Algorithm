import sys

def prime(n):
    nums = [True for _ in range(n + 1)]
    nums[0] = False
    nums[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if nums[i]:
            for j in range(i + i, n + 1, i):
                nums[j] = False
    return nums


n_list = []
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    n_list.append(n)

prime_nums = prime(max(n_list))
for n in n_list:
    f = False
    for i in range(1, len(prime_nums), 2):
        if prime_nums[i] and prime_nums[n - i]:
            print(f"{n} = {i} + {n - i}")
            f = True
            break
    if not f:
        print("Goldbach's conjecture is wrong.")