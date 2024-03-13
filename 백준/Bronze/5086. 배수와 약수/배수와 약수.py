while True:
    a, b = map(int, input().split())
    if not (a + b):
        break
    if a % b == 0 or b % a == 0:
        print("factor" if a < b else "multiple")
    else:
        print("neither")