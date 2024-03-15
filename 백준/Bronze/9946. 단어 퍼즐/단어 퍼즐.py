import sys
t = 1
while True:
    case = [sys.stdin.readline()[:-1] for _ in range(2)]
    if case[0] == "END":
        exit()
    d = [dict() for _ in range(2)]
    for i in range(2):
        for s in set(case[i]):
            d[i][s] = case[i].count(s)
    print(f"Case {t}: {'same' if d[0] == d[1] else 'different'}")
    t += 1