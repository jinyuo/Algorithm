import re

def solution(new_id):
    allow_str = '[a-z]|[0-9]|-|_|\.'
    max_len = 16
    min_len = 3

    # step - 1
    new_id = new_id.lower()

    # step - 2
    new_id = ''.join(re.findall(allow_str, new_id))

    # step - 3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # step - 4
    while re.search('^\.', new_id):
        new_id = new_id[1:]
    while re.search('\.$', new_id):
        new_id = new_id[:-1]    

    # step - 5
    if not new_id:
        new_id = 'a'

    # step - 6
    if len(new_id) >= max_len:
        new_id = new_id[:max_len - 1]
    while re.search('\.$', new_id):
        new_id = new_id[:-1]    

    # step - 7
    if len(new_id) < min_len:
        new_id += new_id[-1] * min_len
        new_id = new_id[:min_len]

    return new_id