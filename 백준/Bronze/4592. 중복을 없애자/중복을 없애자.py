import sys
while True:
    inp = sys.stdin.readline()[:-1]
    if inp == "0":
        exit()
    li = list(map(int, inp.split()))
    for i in range(2, li[0] + 1):
        if li[i - 1] != li[i]:
            print(li[i - 1], end=" ")
    print(li[-1], "$")