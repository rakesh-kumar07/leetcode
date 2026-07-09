import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num=[str(i) for i in range(1,n+1)]
        # return "".join(num)
        k=k-1
        result=[]
        for i in range (n,0,-1):
            fact=math.factorial(i-1)
            idx=k//fact
            result.append(num.pop(idx))
            k=k%fact
        return "".join(result)

        # for i in range (n-1,1):

        #     for j in range (1,n+1):
        #         y=fact(n-i)*j
        #         if k<=y:
        #             my_list.appen(j)
        #             break            
