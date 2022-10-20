class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        HEX_CHARS = "0123456789abcdef"
        
        if num < 0:
            num = num + (1 << 32)
        
        ans = []
        while num > 0:
            num, d = divmod(num, 16)
            ans.append(HEX_CHARS[d])
            
        return "".join(reversed(ans))