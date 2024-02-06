def solution(bandage, health, attacks):
    max_health = health
    for i, (cur_time, damage) in enumerate(attacks):
        if i > 0:
            gap = cur_time - 1 - attacks[i - 1][0]
            health += bandage[1] * gap + bandage[2] * (gap // bandage[0])
        if health > max_health:
            health = max_health
        health -= damage
        
        if health <= 0:
            return -1
    
    return health