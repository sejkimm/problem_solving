import pandas as pd
from itertools import product

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:

    student_with_subject: pd.DataFrame = (
        pd
        .merge(left=students, right=subjects, how='cross')
    )

    student_attend = (
        examinations
        .groupby(by=['student_id', 'subject_name'])
        ['subject_name']
        .count()
        .reset_index(name='attended_exams')
    )

    output_df: pd.DataFrame = (
        pd
        .merge(
            left=student_with_subject,
            right=(
                student_attend
                .drop_duplicates(subset=['student_id', 'subject_name'])
            ),
            how='left',
            on=(['student_id', 'subject_name']),
        )
        .fillna({'attended_exams': 0})
        .sort_values(by=['student_id', 'subject_name'])
    )

    return output_df.loc[:, ['student_id', 'student_name', 'subject_name', 'attended_exams']]