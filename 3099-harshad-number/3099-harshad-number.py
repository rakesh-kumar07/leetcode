class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        x1=x
        s=0
        while x1>0:
            rem= x1%10
            s+=rem
            x1=x1//10
        return s if x%s==0 else -1
        