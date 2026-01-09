import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:

    customer_agg: pd.DataFrame = (
        customer
        .groupby(by=['visited_on'])
        ['amount']
        .sum()
        .reset_index(name='amount')
    )

    customer_agg['amount'] = customer_agg['amount'].rolling(window=7).sum()

    return (
        customer_agg
        .query("not amount.isnull()")
        .assign(
            average_amount = round(customer_agg['amount'] / 7, 2)
        )
    )
