class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(i: int, comb: list) -> None:
            if i >= n:
                if comb:
                    ans.append("".join(comb))
            else:
                for c in mapping[digits[i]]:
                    comb.append(c)
                    backtrack(i + 1, comb)
                    comb.pop()       
        
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ans, n = [], len(digits)
        backtrack(0, [])
        return ans