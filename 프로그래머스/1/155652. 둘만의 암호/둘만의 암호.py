def solution(s, skip, index):
    skip = [ord(s) for s in list(skip)]
    rule = {}
    for char in range(ord('a'), ord('z') + 1):
        skip_cnt = 0
        i = 1
        while i <= index:
            if ((char - ord('a') + i + skip_cnt) % 26 + ord('a')) in skip:
                skip_cnt += 1
            else:
                i += 1
        rule[char] = (char - ord('a') + index + skip_cnt) % 26 + ord('a')
    return s.translate(rule)