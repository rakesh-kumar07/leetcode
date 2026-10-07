class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        # Convert to 32-bit unsigned integer equivalent to handle two's complement
        num &= 0xFFFFFFFF
        
        hex_chars = "0123456789abcdef"
        result = []
        
        while num > 0:
            # Get the last 4 bits (1 hex digit)
            digit = num & 0xF
            result.append(hex_chars[digit])
            # Shift right by 4 bits to process the next hex digit
            num >>= 4
            
        return "".join(reversed(result))