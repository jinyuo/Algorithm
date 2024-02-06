def solution(board, h, w):
    size = len(board)
    list_hw = [(-1, 0), (1, 0), (0, 1), (0 , -1)]
    standard_color = board[h][w]
    list_arround = [board[h + mh][w + mw] for mw, mh in list_hw if 0 <= h + mh < size and 0 <= w + mw < size]    
    return list_arround.count(board[h][w])