import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salary=employee['salary'].drop_duplicates()
    sort_salary=unique_salary.sort_values(ascending=False)
    if len(sort_salary)<N or N<=0:
        nth_highest=None
    else:
        nth_highest=sort_salary.iloc[N-1]
    return pd.DataFrame({'getNthHighestSalary'+'('+str(N)+')':[nth_highest]})