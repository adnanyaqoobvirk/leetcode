class Solution:
    def countVowelStrings(self, n: int) -> int:
        def backtrack(comb: int, pos: int) -> int:
            if comb == n:
                return 1
            else:
                ans = 0
                for i in range(pos, 5):
                    ans += backtrack(comb + 1, i)
                return ans
        return backtrack(0, 0)