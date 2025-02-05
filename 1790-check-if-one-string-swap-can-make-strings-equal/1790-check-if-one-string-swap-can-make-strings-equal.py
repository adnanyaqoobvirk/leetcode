class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        chars = ""
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
                if not chars:
                    chars = f"{s1[i]}{s2[i]}"
                elif chars != f"{s2[i]}{s1[i]}":
                    return False
        return diff == 0 or diff == 2
