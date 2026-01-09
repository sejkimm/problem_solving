import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:

    request_agg: pd.DataFrame = (
        request_accepted
        .groupby(by=['requester_id'])
        ['accepter_id']
        .nunique()
        .reset_index(name='friends_count')
        .rename(columns={'requester_id': 'id'})
    )

    accept_agg: pd.DataFrame = (
        request_accepted
        .groupby(by=['accepter_id'])
        ['requester_id']
        .nunique()
        .reset_index(name='friends_count')
        .rename(columns={'accepter_id': 'id'})
    )

    friends_agg: pd.DataFrame = (
        request_agg
        .merge(
            right=accept_agg,
            how='outer',
            on=['id'],
            suffixes=('_request', '_accept')
        )
        .fillna(0)
    )

    return (
        friends_agg
        .assign(
            num = friends_agg['friends_count_request'] + friends_agg['friends_count_accept']
        )
        .sort_values(by=['num'], ascending=False)
        .iloc[[0]]
        .loc[:, ['id', 'num']]
    )

    ## Some examples are broken. The following code is a more suitable solution.
    # relationships: pd.DataFrame = (
    #     pd
    #     .concat(
    #         [
    #             request_accepted
    #             .loc[:, ['requester_id', 'accepter_id']],
    #             request_accepted
    #             .rename(columns={
    #                 'accepter_id': 'requester_id',
    #                 'requester_id': 'accepter_id'})
    #             .loc[:, ['requester_id', 'accepter_id']]
    #         ],
    #         axis=0
    #     )
    # )

    # return (
    #     relationships
    #     .groupby(by=['requester_id'])
    #     ['accepter_id']
    #     .nunique()
    #     .reset_index(name='num')
    #     .sort_values(by=['num'], ascending=False)
    #     .iloc[[0]]
    #     .rename(columns={'requester_id': 'id'})
    # )
