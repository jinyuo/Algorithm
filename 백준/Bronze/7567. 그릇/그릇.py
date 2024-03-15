p = input()
s = 10
for i in range(1, len(p)):
    s += 5 if p[i-1] == p[i] else 10
print(s)