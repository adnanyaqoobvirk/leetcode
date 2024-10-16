class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(i: int) -> bool:
            if i >= n:
                return True

            t = trie
            for j in range(i, n):
                if s[j] not in t:
                    break
                t = t[s[j]]
                if "#" in t and dp(j + 1):
                    return True
            return False

        trie = {}
        for word in wordDict:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = {}
            
        n = len(s)
        return dp(0)
                
