import pandas as pd
from datetime import datetime

def solution(data, ext, val_ext, sort_by):    
    df = pd.DataFrame(data, columns=['code', 'date', 'maximum', 'remain'])
    df['date'] = df.date.apply(lambda x: datetime.strptime(str(x), '%Y%m%d'))
    if ext == 'date':
        val_ext = datetime.strptime(str(val_ext), '%Y%m%d')

    df = df[df[ext] < val_ext].sort_values(sort_by)
    df['date'] = df.date.apply(lambda x: int(datetime.strftime(x, '%Y%m%d')))

    return df.values.tolist()