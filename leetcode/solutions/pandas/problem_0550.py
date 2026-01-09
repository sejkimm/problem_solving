import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    
    activity['login_order'] = (
        activity
        .groupby(by=['player_id'])
        ['event_date']
        .rank(method='min')
    )

    two_consecutive_login_player_count = (
        pd
        .merge(
            left=(
                activity
                .query("login_order == 1")
            ),
            right=(
                activity
                .query("login_order == 2")
            ),
            how='inner',
            on=['player_id'],
            suffixes=['_first', '_second']
        )
        .query("(event_date_second - event_date_first).dt.days == 1")
        .shape[0]
    )

    return (
        pd
        .DataFrame({
            'fraction': [round(two_consecutive_login_player_count / activity['player_id'].dropna().drop_duplicates().shape[0], 2)]
        })
    )
