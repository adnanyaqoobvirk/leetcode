class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        def atMost(vcount: int) -> int:
            ssCount = 0
            seen = {}
            l = 0
            for r in range(len(word)):
                if word[r] not in vowels:
                    seen = {}
                    l = r + 1
                else:
                    seen[word[r]] = seen.get(word[r], 0) + 1
                    while len(seen) > vcount:
                        seen[word[l]] -= 1
                        if seen[word[l]] == 0:
                            del seen[word[l]]
                        l += 1
                    ssCount += r - l + 1
            return ssCount

        vowels = set("aeiou")
        return atMost(5) - atMost(4)