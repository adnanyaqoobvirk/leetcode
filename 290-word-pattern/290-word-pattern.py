class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        
        cw_map, wc_map = {}, {}
        for c, word in zip(pattern, words):
            if c not in cw_map:
                cw_map[c] = word
            if word not in wc_map:
                wc_map[word] = c
                
            if cw_map[c] != word or wc_map[word] != c:
                return False
        return True
            