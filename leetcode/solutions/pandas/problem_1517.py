import pandas as pd
import re

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'

    return (
        users[users['mail'].apply(lambda x: bool(re.match(pattern, x)))]
    )
