import sys
from collections import Counter

word_1 = sys.stdin.readline().strip()
word_2 = sys.stdin.readline().strip()

anagram = sum((Counter(word_1) & Counter(word_2)).values())
total = sum((Counter(word_1) | Counter(word_2)).values())
print(total - anagram)