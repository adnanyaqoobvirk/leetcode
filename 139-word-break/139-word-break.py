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
        dp = [False] * n
        dp.append(True)
        for pos in reversed(range(n)):
            t, i = trie, pos
            while i < n:
                if s[i] in t:
                    t = t[s[i]]
                    if '#' in t and dp[i + 1]:
                        dp[pos] = True
                        break
                    i += 1
                elif '#' in t:
                    t = trie
                else:
                    break
        return dp[0]
            