class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(potions)
        potions.sort()

        ans = []
        for s in spells:
            i = bisect_left(potions, ceil(success / s))
            ans.append(0 if i == n else n - i)
        return ans