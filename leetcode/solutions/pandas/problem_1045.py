import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:

    customer_agg: pd.DataFrame = (
        customer
        .groupby(by=['customer_id'])
        ['product_key']
        .nunique()
        .reset_index(name='bought_products_count')
    )

    total_products: int = len(product)

    return (
        customer_agg
        .query("bought_products_count == @total_products")
        .loc[:, ['customer_id']]
    )
