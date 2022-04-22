while True:
    s = input()
    if s == '#' : break

    k = 0
    for i in range(len(s)):
        if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
            k = i
            break
    print(s[k:] + s[:k] + 'ay')