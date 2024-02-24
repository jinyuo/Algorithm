def solution(data, ext, val_ext, sort_by):
    columns = ['code', 'date', 'maximum', 'remain']           
    data = [d for d in data if d[columns.index(ext)] < val_ext]
    data.sort(key=lambda x: x[columns.index(sort_by)])
    return data