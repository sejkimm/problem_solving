import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    low_salary: int = len(accounts.query("income < 20000"))
    average_salary: int = len(accounts.query("20000 <= income <= 50000"))
    high_salary: int = len(accounts.query("50000 < income"))

    return (
        pd.DataFrame({
            'category': ['Low Salary', 'Average Salary', 'High Salary'],
            'accounts_count': [low_salary, average_salary, high_salary]
        })
    )
