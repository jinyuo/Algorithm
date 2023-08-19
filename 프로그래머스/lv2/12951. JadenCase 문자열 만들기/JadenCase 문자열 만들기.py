import re

def solution(s):
    return re.sub(r'(^|\b)([a-z])', lambda x: x.group(2).upper(), s.lower())