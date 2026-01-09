import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    return (
        orders
        .query("'2020-02-01' <= order_date < '2020-03-01'")
        .groupby(by=['product_id'])
        ['unit']
        .sum()
        .reset_index(name='total_unit')
        .query("total_unit >= 100")
        .merge(
            right=products,
            how='inner',
            on=['product_id']
        )
        .loc[:, ['product_name', 'total_unit']]
        .rename(columns={'total_unit': 'unit'})
    )
