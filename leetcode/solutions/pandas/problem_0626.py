import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    
    seat['new_id'] = (
        seat
        .apply(
            lambda x: x['id'] - 1 if x['id'] % 2 == 0 else (
                x['id'] if x['id'] == len(seat) else x['id'] + 1
            ),
            axis=1         
        )
    )

    return (
        seat
        .loc[:, ['new_id', 'student']]
        .rename(columns={'new_id': 'id'})
        .sort_values(by=['id'])
    )
