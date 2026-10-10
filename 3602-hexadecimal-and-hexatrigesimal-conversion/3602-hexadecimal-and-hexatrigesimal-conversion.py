class Solution:
    def concatHex36(self, n: int) -> str:
        def to_base(num: int, base: int) -> str:
            if num == 0:
                return "0"
            
            chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            res = []
            while num > 0:
                res.append(chars[num % base])
                num //= base
            return "".join(reversed(res))
        
        hex_rep = to_base(n * n, 16)
        hexatrigesimal_rep = to_base(n * n * n, 36)
        
        return hex_rep + hexatrigesimal_rep