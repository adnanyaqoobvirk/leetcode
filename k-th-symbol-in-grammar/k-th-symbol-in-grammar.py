class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(m: int) -> bool:
            if m == 1: return False
            return helper((m + 1) // 2) if m & 1 else not helper(m // 2)
        return int(helper(k))