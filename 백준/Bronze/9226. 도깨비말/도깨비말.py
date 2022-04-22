import sys
vowel = "aeiou"
while True:
    word = sys.stdin.readline()[:-1]
    if word == "#": exit()
    if word[0] in vowel or len([x for x in vowel if x in word]) == 0:
        print(word + "ay")
    else:
        for i in range(len(word)):
            if word[i] in vowel:
                print(word[i:] + word[:i] + "ay")
                break