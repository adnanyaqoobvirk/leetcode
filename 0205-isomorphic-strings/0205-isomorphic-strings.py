class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_ch_map = {}
        t_ch_map = {}
        
        for i in range(len(s)):
            if s[i] not in s_ch_map:
                s_ch_map[s[i]] = t[i]
            if t[i] not in t_ch_map:
                t_ch_map[t[i]] = s[i]
            
            if s_ch_map[s[i]] != t[i] or s[i] != t_ch_map[t[i]]:
                return False
        
        return True