import pandas as pd


def user_activity(activity: pd.DataFrame) -> pd.DataFrame:

    period_end = pd.to_datetime("2019-07-27")
    period_begin = period_end - pd.Timedelta(days=30)

    return (
        activity.query("@period_begin < activity_date <= @period_end")
        .groupby(by=["activity_date"])["user_id"]
        .nunique()
        .reset_index(name="active_users")
        .rename(columns={"activity_date": "day"}, inplace=False)
    )
