import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:

    all_products: pd.DataFrame = (
        products
        .loc[:, ['product_id']]
        .drop_duplicates()
    )

    products['latest_change'] = (
        products
        .query("change_date <= '2019-08-16'")
        .groupby(by=['product_id'])
        ['change_date']
        .rank(method='max', ascending=False)
    )

    return (
        all_products
        .merge(
            right=products.query("latest_change == 1"),
            how='left',
            on=['product_id']
        )
        .loc[:, ['product_id', 'new_price']]
        .fillna({'new_price': 10})
        .rename(columns={'new_price': 'price'})
    )
