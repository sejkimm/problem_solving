import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    user_list: pd.DataFrame = signups.loc[:, ['user_id']]

    user_event_count: pd.DataFrame = (
        confirmations
        .groupby(by=['user_id', 'action'])
        .size()
        .reset_index(name='count')
    )

    user_event_summary: pd.DataFrame = (
        user_list
        .merge(
            right=(
                user_event_count
                .query("action == 'confirmed'")
                .loc[:, ['user_id', 'count']]
            ),
            how='left',
            on=['user_id']
        )
        .rename(columns={"count": "confirmed"})
        .merge(
            right=(
                user_event_count
                .query("action == 'timeout'")
                .loc[:, ['user_id', 'count']]
            ),
            how='left',
            on=['user_id']
        )
        .rename(columns={"count": "timeout"})
        .fillna({"confirmed": 0, "timeout": 0})
    )

    return (
        user_event_summary
        .assign(confirmation_rate = lambda x: (x['confirmed'] / (x['confirmed'] + x['timeout'])))
        .round({"confirmation_rate": 2})
        .loc[:, ['user_id', 'confirmation_rate']]
        .fillna({"confirmation_rate": 0})
    )
