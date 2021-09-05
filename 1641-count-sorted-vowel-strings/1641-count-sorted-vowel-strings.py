class Solution:
    def countVowelStrings(self, n: int) -> int:
        def backtrack(comb: int, pos: int) -> int:
            if comb == n:
                return 1
            else:
                ans = 0
                for i in range(pos, len(vowels)):
                    ans += backtrack(comb + 1, i)
                return ans
        
        vowels = 'aeiou'
        return backtrack(0, 0)