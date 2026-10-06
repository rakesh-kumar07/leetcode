class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Count total 1s and 0s
        ones = s.count('1')
        zeros = s.count('0')
        
        # Place (ones - 1) '1's at the start, followed by all '0's, and 1 '1' at the end
        return '1' * (ones - 1) + '0' * zeros + '1'