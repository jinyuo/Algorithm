import sys

p = int(sys.stdin.readline())
su = ["TTT", "TTH", "THT", "THH", "HTT", "HTH", "HHT", "HHH"]
for _ in range(p):
    coin = sys.stdin.readline()
    co = [0] * 8
    for i in range(len(su)):
        for j in range(len(coin) - 2):
            if coin[j:j + 3] == su[i]:
                co[i] += 1
    print(" ".join(str(s) for s in co))