class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def nextChar(i: int) -> str:
            for ch in char_map[digits[i]]:
                yield ch

        char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        n = len(digits)
        combs = []
        comb = []
        stack = [(0, None)]
        while stack:
            idx, itr = stack.pop()

            if idx >= n:
                combs.append("".join(comb))
                comb.pop()
                continue
            
            if not itr:
                itr = nextChar(idx)
            
            ch = next(itr, None)
            if ch:
                comb.append(ch)
                stack.append((idx, itr))
                stack.append((idx + 1, None))
            elif comb:
                comb.pop()

        return combs