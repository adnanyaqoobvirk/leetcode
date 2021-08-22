class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s) // 2
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        a_count = 0
        b_count = 0
        for i in range(n):
            if s[i] in vowels:
                a_count += 1
            if s[i + n] in vowels:
                b_count += 1
        return a_count == b_count