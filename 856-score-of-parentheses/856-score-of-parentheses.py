class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def helper(i: int) -> int:
            if i >= n:
                return 1
            
            score = 0
            while i < n:
                if s[i] == '(':
                    if s[i + 1] == ')':
                        score += 1
                    else:
                        pscore, i = helper(i + 1)
                        score += 2 * pscore
                else:
                    if s[i - 1] != '(':
                        return score, i                        
                i += 1
            return score, i
        n = len(s)
        return helper(0)[0]