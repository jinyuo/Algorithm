loop = int(input())
for i in range(loop):
    mars = list(input().split())
    num = float(mars.pop(0))
    while mars:
        tmp = mars.pop(0)
        if tmp == '@':
            num *= 3
        elif tmp == '%':
            num += 5
        else:
            num -= 7
    print(f"{num:.2f}")