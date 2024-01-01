import re

def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees:
        tree = ''.join(re.findall(f'[{skill}]', st))
        if skill.startswith(tree):  answer += 1
    return answer