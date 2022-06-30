class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}
        for word in wordDict:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = True
        
        n = len(s)
        
        dp = [False] * (n + 1)
        dp[n] = True
        
        for pos in reversed(range(n)):
            t = trie
            for i in range(pos, n):
                if s[i] not in t:
                    break
                    
                t = t[s[i]]
                if '#' in t and dp[i + 1]:
                    dp[pos] = True
                    break
        return dp[0]