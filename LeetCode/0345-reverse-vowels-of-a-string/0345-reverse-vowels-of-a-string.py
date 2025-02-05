class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        list_s = list(s)
        for i, v in enumerate(s):
            if v in 'aeiouAEIOU':
                vowels.append([i, v])

        for i, v in zip([i[0] for i in vowels], [i[1] for i in vowels][::-1]):
            list_s[i] = v

        return "".join(list_s)