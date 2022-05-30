class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def helper(pos: int) -> bool:
            if pos == n:
                return True
            
            t, i = trie, pos
            while i < n:
                if s[i] in t:
                    t = t[s[i]]
                    if '#' in t and helper(i + 1):
                        return True
                    i += 1
                elif '#' in t:
                    t = trie
                else:
                    break
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