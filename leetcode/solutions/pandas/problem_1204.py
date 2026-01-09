import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:

    queue['total_weight'] = (
        queue
        .sort_values(by=['turn'])
        ['weight']
        .cumsum()
    )

    return (
        queue
        .query("total_weight <= 1000")
        .sort_values(by=['turn'], ascending=False)
        .head(1)
        .loc[:, ['person_name']]
    )
