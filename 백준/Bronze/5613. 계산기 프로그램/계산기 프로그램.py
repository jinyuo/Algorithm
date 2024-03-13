import sys
an, op = 0, ""
while True:
    inp = sys.stdin.readline()[:-1]
    if inp == "=":
        print(an)
        exit()
    if inp.isnumeric():
        an = inp if op == "" else int(eval(f"{an} {op} {inp}"))
    else:
        op = inp