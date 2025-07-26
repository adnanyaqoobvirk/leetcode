class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        starts = defaultdict(list)
        for start, end in conflictingPairs:
            starts[max(start, end)].append(min(start, end))
        
        ans = 0
        base = 0
        left = right = 0
        bonuses = [0] * (n + 1)
        for i in range(1, n + 1):
            for v in starts[i]:
                if v > right:
                    left, right = right, v
                elif v > left:
                    left = v
            
            base += i - right
            bonuses[right] += right - left
        return base + max(bonuses)