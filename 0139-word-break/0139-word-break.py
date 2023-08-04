class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(i: int) -> bool:
            if i >= n:
                return True
            
            for j in range(i + 1, n + 1):
                if s[i:j] in wordSet and dp(j):
                    return True
            return False
        
        n = len(s)
        wordSet = set(wordDict)
        return dp(0)