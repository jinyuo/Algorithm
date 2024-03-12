import sys
fr = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
inp = sys.stdin.readline()[:-1]
l = sum([fr.index(i) for i in inp])
divider = 2
while divider * divider <= l:
    if l % divider == 0:
        print("It is not a prime word.")
        exit()
    else:
        divider += 2 if divider > 2 else 1
print("It is a prime word.")