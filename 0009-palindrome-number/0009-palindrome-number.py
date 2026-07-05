class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x=str(x)
        if str_x[::-1]==str_x:
            return True
        else:
            return False