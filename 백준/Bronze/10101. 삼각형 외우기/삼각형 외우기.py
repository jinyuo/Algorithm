import sys
li = [int(sys.stdin.readline()) for _ in range(3)]
li.sort()
if sum(li) != 180:
    print("Error")
else:
    print(["", "Scalene", "Isosceles", "Equilateral"][li.count(li[1])])
