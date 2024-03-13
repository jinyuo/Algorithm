import sys
caesar = sys.stdin.readline()[:-1]
decode = ""
for c in caesar:
    if "A" <= c <= "Z":
        d = ord(c) - 3
        decode += chr(d) if d >= ord("A") else chr(ord("Z") - ord("A") + d + 1)
print(decode)
