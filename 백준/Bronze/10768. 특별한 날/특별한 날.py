import sys
import time
m = int(sys.stdin.readline())
d = int(sys.stdin.readline())
i = time.strptime(f"2015-{m}-{d}", "%Y-%m-%d")
s = time.strptime(f"2015-2-18", "%Y-%m-%d")
print("Special" if i == s else "Before" if i < s else "After")