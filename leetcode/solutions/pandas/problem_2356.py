import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:

    return (
        teacher
        .groupby(by=['teacher_id'], dropna=False)['subject_id']
        .nunique()
        .reset_index(name='cnt')
    )
