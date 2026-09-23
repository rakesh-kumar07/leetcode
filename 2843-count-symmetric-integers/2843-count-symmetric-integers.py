class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        
        for num in range(low, high + 1):
            s = str(num)
            n = len(s)
            
            # Symmetric numbers must have an even number of digits
            if n % 2 != 0:
                continue
            
            half = n // 2
            first_half_sum = sum(int(d) for d in s[:half])
            second_half_sum = sum(int(d) for d in s[half:])
            
            if first_half_sum == second_half_sum:
                count += 1
                
        return count