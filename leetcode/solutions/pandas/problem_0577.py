import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    return (
        pd
        .merge(left=employee, right=bonus, how='left', left_on=['empId'], right_on=['empId'])
        .query("bonus.isnull() or bonus < 1000")
        .loc[:,['name', 'bonus']]
    )