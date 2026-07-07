class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_nbr=[]
        for i in range(left,right+1):
            dividend = i
            flag=True
            while dividend>0:
                rem=dividend%10
                if rem==0 or i%rem!=0:
                    flag=False
                    break
                dividend=dividend//10
            if flag:
                self_nbr.append(i)
        return self_nbr

            