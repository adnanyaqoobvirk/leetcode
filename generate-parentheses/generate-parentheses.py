class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(ocount: int, ccount: int) -> None:
            if ccount > ocount or ocount > n or ccount > n:
                return
            elif ocount == n == ccount:
                ans.append("".join(comb))
            else:
                for p in "()":
                    comb.append(p)
                    if p == "(":
                        backtrack(ocount + 1, ccount)
                    else:
                        backtrack(ocount, ccount + 1)
                    comb.pop()
        ans, comb = [], []
        backtrack(0, 0)
        return ans
        