import re

def solution(new_id):
    allow_str = '[^a-z0-9\-_\.]'
    max_len = 16
    min_len = 3
    
    new_id = new_id.lower()
    new_id = re.sub(allow_str, '', new_id)
    new_id = re.sub('\.+', '.', new_id)
    new_id = re.sub('^\.|\.$', '', new_id)
    
    if not new_id:
        new_id = 'a'
    elif len(new_id) >= max_len:
        new_id = new_id[:max_len - 1]
    new_id = re.sub('\.$', '', new_id)

    if len(new_id) < min_len:
        new_id = (new_id + new_id[-1] * min_len)[:min_len]
    
    return new_id