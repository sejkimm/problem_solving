import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:

    insurance['not_unique_tiv_2015']: pd.DataFrame = (
        insurance
        .groupby(by=['tiv_2015'])
        ['pid']
        .filter(lambda x: len(x) > 1)
    )

    insurance['unique_lat_lon']: pd.DataFrame = (
        insurance
        .groupby(by=['lat', 'lon'])
        ['pid']
        .filter(lambda x: len(x) == 1)
    )

    return (
        pd.DataFrame({
            'tiv_2016': [
                insurance
                .query("not not_unique_tiv_2015.isnull() and not unique_lat_lon.isnull()")
                ['tiv_2016']
                .sum()
                .round(2)
            ]
        })
    )
