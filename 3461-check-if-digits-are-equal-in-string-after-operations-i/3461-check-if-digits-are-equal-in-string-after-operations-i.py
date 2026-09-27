class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Convert string of digits into a list of integers
        digits = [int(ch) for ch in s]
        
        # Continuously reduce the list until exactly 2 digits remain
        while len(digits) > 2:
            next_digits = []
            for i in range(len(digits) - 1):
                next_digits.append((digits[i] + digits[i + 1]) % 10)
            digits = next_digits
            
        # Return True if the final two digits are equal
        return digits[0] == digits[1]