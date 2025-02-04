class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = max(len(word1), len(word2))
        word1 = word1.ljust(length, ' ')
        word2 = word2.ljust(length, ' ')
        
        return ("".join(f"{'' if w1 == ' ' else w1}{'' if w2 == ' ' else w2}" for w1, w2 in zip(word1, word2)))