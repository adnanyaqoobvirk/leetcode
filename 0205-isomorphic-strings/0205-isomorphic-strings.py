class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}
        mapped = set()
        for i in range(len(s)):
            if s[i] not in char_map:
                if t[i] in mapped:
                    return False
                char_map[s[i]] = t[i]
                mapped.add(t[i])
            if char_map[s[i]] != t[i]:
                return False
        return True