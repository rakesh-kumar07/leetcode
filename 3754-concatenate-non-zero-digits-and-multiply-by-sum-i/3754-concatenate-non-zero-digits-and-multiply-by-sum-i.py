class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Step 1: Convert to string and filter out non-zero characters
        non_zero_chars = [ch for ch in str(n) if ch != '0']
        
        # If there are no non-zero digits, x = 0
        if not non_zero_chars:
            return 0
            
        # Step 2: Form integer x by concatenating non-zero digits
        x = int("".join(non_zero_chars))
        
        # Step 3: Compute the sum of digits in x
        digit_sum = sum(int(ch) for ch in non_zero_chars)
        
        # Step 4: Return x * sum
        return x * digit_sum