import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df=employee.merge(
        employee,
        left_on='managerId',
        right_on='id',
        suffixes=('_emp','_mgr')
    )
    df=df[df['salary_emp']>df['salary_mgr']]
    return df[['name_emp']].rename(columns={'name_emp':'Employee'})