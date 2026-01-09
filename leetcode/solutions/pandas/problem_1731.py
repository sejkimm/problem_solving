import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    
    managers: pd.DataFrame = (
        employees
        .groupby(by=['reports_to'])
        .agg(
            employee_id=('reports_to', 'mean'),
            reports_count=('reports_to', 'count'),
            average_age=('age', lambda x: np.mean(x+0.0001).round(0))
        )
    )

    return (
        employees
        .merge(
            right=managers,
            how='inner',
            on=['employee_id']
        )
        .loc[:, ['employee_id', 'name', 'reports_count', 'average_age']]
        .sort_values(by=['employee_id'])
    )