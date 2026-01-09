import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    
    delivery['order_rank'] = (
        delivery
        .groupby(by=['customer_id'], dropna=False)
        ['order_date']
        .rank(method='min')

        # Below code is also correct and more descriptive but slower
        # .transform(
        #     lambda x: x.rank(method='min')
        # )
    )

    delivery_first_order = (
        delivery
        .query("order_rank == 1")
    )

    delivery_first_order['is_immediate_order'] = (
        delivery_first_order
        .apply(
            lambda x: x['order_date'] == x['customer_pref_delivery_date'],
            axis=1
        )
    )

    return (
        pd
        .DataFrame({
            'immediate_percentage': [round(sum(delivery_first_order['is_immediate_order']) / delivery_first_order.shape[0] * 100, 2)]
        })
    )
