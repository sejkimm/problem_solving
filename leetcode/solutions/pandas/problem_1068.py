import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    return (
        pd
        .merge(left=sales, right=product, how='inner', left_on=['product_id'], right_on=['product_id'])
        .loc[:,['product_name', 'year', 'price']]
    )