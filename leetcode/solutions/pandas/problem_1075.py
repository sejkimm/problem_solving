import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    
    project_list: pd.DataFrame = (
        project
        .loc[:, ['project_id']]
        .drop_duplicates()
    )

    project_employee_yoe: pd.DataFrame = (
        project
        .merge(
            right=employee,
            how='left',
            on=['employee_id']
        )
    )

    project_agg: pd.DataFrame = (
        project_employee_yoe
        .groupby(by=['project_id'])
        ['experience_years']
        .apply(lambda x: round(x.mean(), 2))
        .reset_index(name='average_years')
    )

    return (
        project_list
        .merge(
            right=project_agg,
            how='left',
            on=['project_id']
        )
        .fillna({'average_years': 0})
    )