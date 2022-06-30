class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def helper(pos: int) -> bool:
            if pos == n:
                return True
            
            t = trie
            for i in range(pos, n):
                if s[i] not in t:
                    return False
                
                t = t[s[i]]
                if '#' in t and helper(i + 1):
                    return True
            return False
                    
        trie = {}
        for word in wordDict:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = True
        
        n = len(s)
        return helper(0)