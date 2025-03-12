class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        idx = [i for i in range(len(s1)) if s1[i] != s2[i]]
        if not idx:
            return True
        elif len(idx) != 2:
            return False

        s2 = list(s2)
        s2[idx[0]], s2[idx[1]] = s2[idx[1]], s2[idx[0]]
        s2 = "".join(s2)

        return s1 == s2