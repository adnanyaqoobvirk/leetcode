class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        for ss in range((1 << n) + 1):
            p1 = p2 = 1
            for i in range(n):
                if ss & (1 << i):
                    p1 *= nums[i]
                else:
                    p2 *= nums[i]
            if p1 == target == p2:
                return True
        return False