import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    
    min_id: int = logs.min(axis=0)['id'] if not logs.empty else 0

    logs_1before: pd.DataFrame = logs.query("id >= @min_id + 1").assign(id=logs['id'] - 1)
    logs_2before: pd.DataFrame = logs.query("id >= @min_id + 2").assign(id=logs['id'] - 2)

    return (
        logs
        .merge(right=logs_1before, how='inner', on=['id'], suffixes=(None, '_1before'))
        .merge(right=logs_2before, how='inner', on=['id'], suffixes=(None, '_2before'))
        .query("num == num_1before and num == num_2before")
        .loc[:, ['num']]
        .drop_duplicates()
        .rename(columns={'num': 'ConsecutiveNums'})
    )
