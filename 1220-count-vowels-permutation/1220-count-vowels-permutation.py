class Solution:
    def countVowelPermutation(self, n: int) -> int:
        @cache
        def helper(pos: int, pchar: str) -> int:
            if pos == 0:
                return 1
            
            if pchar == 'a':
                return helper(pos - 1, 'e') % MOD
            elif pchar == 'e':
                return (helper(pos - 1, 'a') + helper(pos - 1, 'i')) % MOD
            elif pchar == 'i':
                return sum(helper(pos - 1, ch) for ch in 'aeou') % MOD
            elif pchar == 'o':
                return (helper(pos - 1, 'i') + helper(pos - 1, 'u')) % MOD
            elif pchar == 'u':
                return helper(pos - 1, 'a') % MOD
            else:
                return sum(helper(pos - 1, ch) for ch in 'aeiou') % MOD
        
        MOD = 10**9 + 7
        return helper(n, '#')