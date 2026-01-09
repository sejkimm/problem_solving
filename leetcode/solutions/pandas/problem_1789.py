import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:

    employee['department_count'] = (
        employee
        .groupby(by=['employee_id'])
        ['department_id']
        .transform(lambda x: len(x))
    )

    return (
        employee[(employee['department_count'] == 1) | (employee['primary_flag'] == 'Y')]
        .loc[:, ['employee_id', 'department_id']]
    )

    # more complicated solution


    # one_department: pd.DataFrame = employee["employee_id"].drop_duplicates(keep=False).reset_index(name="employee_id")

    # primary_department: pd.DataFrame = employee.query("primary_flag == 'Y'").loc[:, ["employee_id", "department_id"]]

    # return (
    #     pd
    #     .concat(
    #         [
    #             (
    #                 employee
    #                 .merge(
    #                     right=one_department,
    #                     how="inner",
    #                     on=["employee_id"]
    #                 )
    #                 .loc[:, ['employee_id', 'department_id']]
    #             ),
    #             primary_department
    #         ]
    #         , axis=0
    #     )
    # )
