import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    
    return (
        pd
        .merge(left=employees, right=employee_uni, how='left', left_on=['id'], right_on=['id'])
        .loc[:, ['unique_id', 'name']]
    )