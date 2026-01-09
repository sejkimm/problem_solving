import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    
    user_count: int = len(users)

    return (
        register
        .groupby(by=['contest_id'])
        ['user_id']
        .count()
        .transform(lambda x: round(x / user_count * 100, 2))
        .reset_index(name='percentage')
        .sort_values(by=['percentage', 'contest_id'], ascending=[False, True])
    )