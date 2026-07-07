class Solution:
    def convertToBase7(self, num: int) -> str:
        if num ==0:
            return "0"
        is_negative = num<0
        x=abs(num)
        digits=[]
        while x>0:
            reminder = x%7
            digits.append(str(reminder))
            x=x//7
        result="".join(reversed(digits))
        return f"-{result}" if is_negative else result