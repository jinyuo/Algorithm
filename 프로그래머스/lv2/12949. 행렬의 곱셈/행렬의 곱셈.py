def solution(arr1, arr2):
    rows = len(arr1)
    cols = len(arr2[0])
    answer = [[-1 for i in range(cols)] for j in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            arr1_a = arr1[i]
            arr2_b = [a[j] for a in arr2]
            answer[i][j] = sum([arr1_a[t] * arr2_b[t] for t in range(len(arr1_a))])    
    
    return answer