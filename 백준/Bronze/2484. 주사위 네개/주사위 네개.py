import sys
n = int(sys.stdin.readline())
m = []
for _ in range(n):
    dice = sorted(list(map(int, sys.stdin.readline().split())))
    len_dice = len(set(dice))
    if len_dice == 1:
        m.append(50000 + 5000 * dice[3])
    elif len_dice == 2:
        m.append(10000 + 1000 * dice[2] if dice[1] == dice[2] else 2000 + 500 * dice[1] + 500 * dice[2])
    elif len_dice == 3:
        m.append(1000 + dice[0] * 100 if dice[0] == dice[1] else (
            1000 + dice[1] * 100 if dice[1] == dice[2] else 1000 + dice[2] * 100))
    else:
        m.append(dice[3] * 100)
print(max(m))