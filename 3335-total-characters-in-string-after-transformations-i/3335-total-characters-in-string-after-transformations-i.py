class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cmap = [0] * 26
        for c in s:
            cmap[ord(c) - ord('a')] += 1

        for _ in range(t):
            ncmap = [0] * 26
            for i in range(26):
                if i == 25:
                    ncmap[0] += cmap[i]
                    ncmap[1] += cmap[i]
                else:
                    ncmap[i + 1] += cmap[i]
            cmap = ncmap
        return sum(cmap) % (10**9+7)