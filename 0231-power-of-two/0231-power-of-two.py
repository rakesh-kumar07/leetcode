class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0 :
            return False

        for i in range (n):
            j=pow(2,i)
            
            if j==n: 
                return True
                break
            if j>n: 
                return False
                break
