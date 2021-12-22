class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        
        s1_char_map, s2_char_set = {}, set()
        for c1, c2 in zip(str1, str2):
            if s1_char_map.setdefault(c1, c2) != c2:
                return False
            s2_char_set.add(c2)
        return len(s2_char_set) < 26