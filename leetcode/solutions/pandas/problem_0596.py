import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:

    return (
        courses
        .groupby(by=['class'])
        .filter(lambda x: len(x) >= 5)
        .loc[:, ['class']]
        .drop_duplicates()
    )
