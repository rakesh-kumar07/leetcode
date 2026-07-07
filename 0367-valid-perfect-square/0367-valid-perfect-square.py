class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<=3 and num!=1:
            return False
        if num==1 :
            return True
        for i in range (num):
            j=i*i
            
            if j==num: 
                return True
                break
            if j>num: 
                return False
                break