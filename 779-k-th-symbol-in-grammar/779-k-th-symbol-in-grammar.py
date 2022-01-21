class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1: return 0
        
        if k & 1: return self.kthGrammar(n, math.ceil(k / 2))
        else: return int(not self.kthGrammar(n, k // 2))