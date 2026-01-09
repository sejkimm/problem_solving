import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    
    duplicated_num: pd.DataFrame = (
        my_numbers
        .groupby(by=['num'], as_index=False)
        ['num']
        .filter(lambda x: len(x) > 1)
        .drop_duplicates()
    )

    try:
        largest_single_number = (
            my_numbers
            .merge(
                right=duplicated_num,
                how='left',
                on='num',
                indicator=True
            )
            .query("_merge == 'left_only'")
            .sort_values(by='num', ascending=False)
            .reset_index()
            .loc[0, 'num']
        )
    except KeyError:
        largest_single_number = pd.NA

    return (
        pd
        .DataFrame({
            'num': [largest_single_number]
        })
    )

    # more consice solution

    # return (
    #     my_numbers
    #     .drop_duplicates(keep=False)
    #     .max()
    #     .to_frame(name='num')
    # )
