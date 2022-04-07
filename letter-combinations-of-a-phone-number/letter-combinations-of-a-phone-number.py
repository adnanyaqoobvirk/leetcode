class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def helper(pos: int) -> None:
            if len(comb) == n:
                ans.append("".join(comb))
            else:
                for c in digit_map[digits[pos]]:
                    comb.append(c)
                    helper(pos + 1)
                    comb.pop()
        n, ans, comb = len(digits), [], []
        helper(0)
        return ans