import sys
def check_tall(tall):
    for i in range(9):
        for j in range(i + 1, 9):
            if sum(tall) - tall[i] - tall[j] == 100:
                tall.pop(j)
                tall.pop(i)
                return tall


tall = check_tall(sorted([int(sys.stdin.readline()) for _ in range(9)]))
print("\n".join(str(i) for i in tall))