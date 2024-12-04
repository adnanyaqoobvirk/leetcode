class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n = len(str1)
        i = 0
        for c in str2:
            for j in range(i, n):
                i = j + 1
                if str1[j] != c:
                    if c == 'a' and str1[j] == 'z':
                        break
                    elif str1[j] == chr(ord(c) - 1):
                        break
                else:
                    break
            else:
                return False
        return True