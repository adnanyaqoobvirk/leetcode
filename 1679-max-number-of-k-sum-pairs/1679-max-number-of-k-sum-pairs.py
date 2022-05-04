class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ops, counts = 0, Counter(nums)
        for num in counts:
            pair = k - num
            if pair == num:
                ops += counts[num] // 2
            elif pair in counts:
                ops += min(counts[pair], counts[num])
                counts[pair] = 0
        return ops