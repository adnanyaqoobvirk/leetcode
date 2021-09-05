class Solution:
    def countVowelStrings(self, n: int) -> int:
        @cache
        def recurse(c: int, pos: int) -> int:
            if c == 1:
                return pos
            
            if pos == 1:
                return 1
            
            return recurse(c - 1, pos) + recurse(c, pos - 1)
        
        return recurse(n, 5)