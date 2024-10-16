class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}
        for word in wordDict:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = {}
            
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        for i in reversed(range(n)):
            t = trie
            for j in range(i, n):
                if s[j] not in t:
                    break
                t = t[s[j]]
                if '#' in t and dp[j + 1]:
                    dp[i] = True
                    break
        return dp[0]
                
