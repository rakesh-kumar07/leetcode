class Solution:
    def totalMoney(self, n: int) -> int:
        rem=n%7
        week=n//7
        week_sum=28*week+7*(week*(week-1)//2)
        day_sum=rem*week+(rem*(rem+1)//2)
        return week_sum+day_sum