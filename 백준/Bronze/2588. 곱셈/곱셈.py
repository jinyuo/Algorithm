a = int(input())
b = input()
sum = 0

for n in range(len(b) - 1, -1, -1):
    r = a * int(b[n])
    print(r)
    sum += r * pow(10, len(b) - 1 - int(n))

print(sum)