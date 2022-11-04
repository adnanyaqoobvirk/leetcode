class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        
        ans = []
        v = len(s) - 1
        for c in s:
            if c not in vowels:
                ans.append(c)
            else:
                while v >= 0 and s[v] not in vowels:
                    v -= 1
                ans.append(s[v])
                v -= 1
        return "".join(ans)