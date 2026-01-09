import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    filtered_managers: pd.DataFrame = (
        employee
        .groupby(by=['managerId'])
        .filter(lambda x: len(x) >= 5)
        .loc[:, ['managerId']]
        .drop_duplicates()
    )

    return (
        pd
        .merge(
            left=employee,
            right=filtered_managers,
            how='inner',
            left_on=['id'],
            right_on=['managerId']
        )
        .loc[:, ['name']]
    )
