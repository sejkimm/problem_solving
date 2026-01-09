import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:

    return (
        employees
        [~employees['manager_id'].isin(employees['employee_id'])]
        .query("salary < 30000 and not manager_id.isnull()")
        .loc[:, ['employee_id']]
        .sort_values(by=['employee_id'])
    )
