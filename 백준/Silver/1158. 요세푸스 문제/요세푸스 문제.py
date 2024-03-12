import sys
n, k = map(int, sys.stdin.readline().split())
people = [i for i in range(1, n + 1)]
yo = list()
i = 0
while people:
    i = (i + k - 1) % (len(people))
    p = people[i]
    yo.append(p)
    people.remove(p)
print("<" + ", ".join(str(i) for i in yo) + ">")