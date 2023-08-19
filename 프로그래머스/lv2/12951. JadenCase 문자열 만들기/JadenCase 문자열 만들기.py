import re

def solution(s):
    return re.sub(r'(^[a-z]|\b[a-z])', lambda x: x.group(1).upper(), s.lower())