import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:

    sales['sales_year_order'] = (
        sales
        .groupby(by=['product_id'])
        ['year']
        .rank(method='min')
    )

    sales_first_year: pd.DataFrame = (
        sales
        .query("sales_year_order == 1")
    )

    return (
        sales_first_year
        .rename(columns={'year': 'first_year'}, inplace=False)
        .loc[:, ['product_id', 'first_year', 'quantity', 'price']]
    )
