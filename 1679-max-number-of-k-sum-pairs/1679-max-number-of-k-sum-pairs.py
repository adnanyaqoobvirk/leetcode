class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ops, counts = 0, defaultdict(int)
        for num in nums:
            comp = k - num
            if counts[comp] > 0:
                ops += 1
                counts[comp] -= 1
            else:
                counts[num] += 1
        return ops