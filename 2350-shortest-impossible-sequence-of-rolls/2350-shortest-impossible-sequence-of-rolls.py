class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen = set()
        ans = 1
        for roll in rolls:
            seen.add(roll)
            
            if len(seen) == k:
                seen = set()
                ans += 1
        return ans