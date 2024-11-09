class Solution:
    def countDistinct(self, s: str) -> int:
        n = len(s)
        dup = 0
        trie = {}
        for i in range(n):
            t = trie
            for j in range(i, n):
                if s[j] not in t:
                    t[s[j]] = {}
                t = t[s[j]]
                if '#' in t:
                    dup += 1
                else:
                    t["#"] = {}
        return (n * (n + 1) // 2) - dup