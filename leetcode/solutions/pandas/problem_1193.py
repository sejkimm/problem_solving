import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:

    transactions_monthly: pd.DataFrame = (
        transactions
        .assign(
            month=lambda x: x['trans_date'].dt.strftime('%Y-%m')
        )
    )

    transactions_total_agg: pd.DataFrame = (
        transactions_monthly
        .groupby(by=['month', 'country'], as_index=False, dropna=False)
        .agg(
            trans_count=('country', lambda x: x.size),
            trans_total_amount=('amount', 'sum')
        )
    )

    transactions_approved_agg: pd.DataFrame = (
        transactions_monthly
        .query("state == 'approved'")
        .groupby(by=['month', 'country'], as_index=False, dropna=False)
        .agg(
            approved_count=('country', lambda x: x.size),
            approved_total_amount=('amount', 'sum')
        )
    )

    return (
        transactions_total_agg
        .merge(
            right=transactions_approved_agg,
            how='outer',
            on=['month', 'country']
        )
        .fillna({
            "trans_count": 0,
            "trans_total_amount": 0,
            "approved_count": 0,
            "approved_total_amount": 0
        })
        .loc[:, ['month', 'country', 'trans_count', 'approved_count', 'trans_total_amount', 'approved_total_amount']]
    )