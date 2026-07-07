import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salary=employee['salary'].drop_duplicates()
    sort_salary=unique_salary.sort_values(ascending=False)
    if len(sort_salary)<2:
        second_highest=None
    else:
        second_highest=sort_salary.iloc[1]
    return pd.DataFrame({'SecondHighestSalary':[second_highest]})