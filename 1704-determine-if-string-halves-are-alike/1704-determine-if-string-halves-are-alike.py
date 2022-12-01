class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        vowels = set('aeiou')

        avowels = bvowels = 0
        for i, j in zip(range(len(s) // 2), range(len(s) // 2, len(s))):
            if s[i] in vowels:
                avowels += 1
                
            if s[j] in vowels:
                bvowels += 1
        return avowels == bvowels