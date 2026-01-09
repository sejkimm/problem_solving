import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:

    best_user = (
        movie_rating
        .groupby(by=['user_id'])
        ['movie_id']
        .count()
        .reset_index(name='movie_count')
        .merge(
            right=users,
            how='inner',
            on=['user_id']
        )
        .sort_values(by=['movie_count', 'name'], ascending=[False, True])
        .head(1)
        .name
    )

    best_movie = (
        movie_rating
        .query("'2020-02-01' <= created_at < '2020-03-01'")
        .groupby(by=['movie_id'])
        ['rating']
        .mean()
        .reset_index(name='avg_rating')
        .merge(
            right=movies,
            how='inner',
            on=['movie_id']
        )
        .sort_values(by=['avg_rating', 'title'], ascending=[False, True])
        .head(1)
        .title
    )

    return (
        pd
        .concat([best_user, best_movie], axis=0)
        .reset_index(name='results')
        .loc[:, ['results']]
    )
