class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack():
            ans = 1
            for k in counts:
                if counts[k] > 0:
                    counts[k] -= 1
                    ans += backtrack()
                    counts[k] += 1
            return ans
        counts = Counter(tiles)
        return backtrack() - 1