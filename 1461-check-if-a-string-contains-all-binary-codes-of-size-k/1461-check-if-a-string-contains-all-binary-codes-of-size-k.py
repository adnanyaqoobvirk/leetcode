class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        MAX_SET_SIZE = 1 << k
        
        ss = set()
        for i in range(len(s) - k + 1):
            if len(ss) == MAX_SET_SIZE:
                break
            ss.add(int(s[i:i + k], 2))
        
        for code in range(MAX_SET_SIZE):
            if code not in ss:
                return False
        return True