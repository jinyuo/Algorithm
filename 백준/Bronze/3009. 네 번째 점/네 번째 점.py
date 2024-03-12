x = []
y = []
for i in range(3):
    an = input().split()
    x.append(an[0])
    y.append(an[1])

for i in range(3):
    if x.count(x[i]) == 1:
        x.append(x[i])
    if y.count(y[i]) == 1:
        y.append(y[i])

print(f"{x[-1]} {y[-1]}")