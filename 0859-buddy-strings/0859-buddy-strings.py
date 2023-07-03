class Solution:
    def buddyStrings(self, s: str, g: str) -> bool:
        c = 0
        for i in range(len(s)):
            if s[i] != g[i]:
                c += 1
        if c == 2:
            return Counter(s) == Counter(g)
        elif c == 0:
            return Counter(s).most_common(1)[0][1] > 1
        else:
            return False