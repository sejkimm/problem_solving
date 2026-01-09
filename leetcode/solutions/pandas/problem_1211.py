import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    from decimal import Decimal, ROUND_HALF_UP

    queries_quality_agg: pd.DataFrame = (
        queries
        .assign(row_quality = queries['rating'] / queries['position'])
        .groupby(by=['query_name'])
        .apply(
            lambda x: Decimal(x['row_quality'].sum() / x.shape[0]).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        )
        .reset_index(name='quality')
    )

    queries_poor_agg: pd.DataFrame = (
        queries
        .groupby(by=['query_name'])
        .apply(
            lambda x: Decimal(x.query("rating < 3").shape[0] / x.shape[0] * 100).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        )
        .reset_index(name='poor_query_percentage')
    )

    return (
        queries_quality_agg
        .merge(
            right=queries_poor_agg,
            how='outer',
            on='query_name'
        )
        .sort_values(by=['query_name'])
    )


# My comment

# There is an inconsistency with`round()` method in python (when solving this problem use Pandas) due to the limitation of floating point representation. 
# In my case, `round(0.325000...., 2)` returned `0.32` instead of `0.33` because `0.325000....` was actually `0.324999...` when expressed in binary.
# To resolve this issue, it is recommended to use 'Decimal' module as follows 
#  ```
# from decimal import Decimal, ROUND_HALF_UP
# Decimal(0.325....).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
# ```
# or use an epsilon like
# `round(0.325.... + 1e-09, 2)`
# The first method is considered better practice but much slower than native. 


# SQL Solution (PostgreSQL)

# WITH Queries_quality_agg AS (
#     SELECT query_name, ROUND(SUM(row_quality)::decimal / COUNT(row_quality), 2) AS quality
#     FROM (
#         SELECT query_name, rating::decimal / position AS row_quality
#         FROM Queries
#     )
#     GROUP BY query_name
# ), Queries_poor_agg AS (
#     SELECT query_name, ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END)::decimal * 100 / COUNT(rating), 2) AS poor_query_percentage
#     FROM Queries
#     GROUP BY query_name
# )
# SELECT
#     query_name, quality, poor_query_percentage
# FROM Queries_quality_agg
# INNER JOIN Queries_poor_agg
# USING (query_name)
# ORDER BY query_name