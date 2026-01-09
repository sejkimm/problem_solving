import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:

    return (
        followers
        .groupby(by=['user_id'])
        ['follower_id']
        .count()
        .reset_index(name='followers_count')
    )
