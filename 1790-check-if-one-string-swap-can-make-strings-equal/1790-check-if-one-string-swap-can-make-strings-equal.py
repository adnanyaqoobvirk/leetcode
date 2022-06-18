class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1_char = s2_char = None
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1_char is not None and (s1_char != s2[i] or s2_char != s1[i]):
                    return False
                s1_char, s2_char = s1[i], s2[i]
                diff += 1
        return diff == 2 or diff == 0