class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        S="123456789"
        num_out=[]
        for i in range (2,10):
            for j in range (len(S)-i+1):
                num=int(S[j:j+i])
                if low <= num <= high:
                    num_out.append(num)
        return num_out