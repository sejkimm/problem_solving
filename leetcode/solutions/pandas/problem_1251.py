import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    
    products: pd.DataFrame = (
        prices
        .loc[:, ['product_id']]
        .drop_duplicates()
    )

    purchase_event: pd.DataFrame = (
        prices
        .merge(
            right=units_sold,
            how='left',
            on=['product_id']
        )
        .query("start_date <= purchase_date <= end_date")
    )

    purchase_agg: pd.DataFrame = (
        purchase_event
        .groupby(by=['product_id'])
        .apply(
            lambda x: round(sum(x['units'] * x['price']) / sum(x['units']), 2)
        )
        .reset_index(name='average_price')
    )

    return (
        products
        .merge(
            right=purchase_agg,
            how='left',
            on=['product_id']
        )
        .fillna({'average_price': 0})
    )