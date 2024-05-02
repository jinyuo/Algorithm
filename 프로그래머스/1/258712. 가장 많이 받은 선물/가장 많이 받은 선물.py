def make_gift_table(friends, gifts):
    num_friends = len(friends)
    table_gifts = [[0 for _ in range(num_friends + 1)] for _ in range(num_friends)]
    for gift in gifts:
        sender, receiver = gift.split()
        table_gifts[friends.index(sender)][friends.index(receiver)] += 1
    
    for i, data in enumerate(table_gifts):    
        table_gifts[i][num_friends] = sum(data) - sum([g[i] for g in table_gifts])
    return table_gifts

def solution(friends, gifts):
    answer = 0
    num_friends = len(friends)
    table_gifts = make_gift_table(friends, gifts)
    
    list_gifts = [0 for _ in range(num_friends)]    
    for i in range(num_friends):
        for j in range(i + 1, num_friends):
            if (table_gifts[i][j] != 0 or table_gifts[j][i] != 0) and (table_gifts[i][j] != table_gifts[j][i]):
                list_gifts[i if table_gifts[i][j] > table_gifts[j][i] else j] += 1
            else:
                if table_gifts[i][num_friends] > table_gifts[j][num_friends]:
                    list_gifts[i] += 1
                elif table_gifts[i][num_friends] < table_gifts[j][num_friends]:
                    list_gifts[j] += 1
    return max(list_gifts)