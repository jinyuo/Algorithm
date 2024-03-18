v = int(input())
p = input()
a = p.count("A")
b = p.count("B")
if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("Tie")