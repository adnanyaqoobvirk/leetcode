class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        num_char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def helper(i: int) -> None:
            if i == n:
                ans.append("".join(comb))
            else:
                for c in num_char_map[digits[i]]:
                    comb.append(c)
                    helper(i + 1)
                    comb.pop()
        
        n, ans, comb = len(digits), [], []
        helper(0)
        return ans