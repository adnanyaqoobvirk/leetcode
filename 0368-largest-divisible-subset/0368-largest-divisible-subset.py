class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        @cache
        def helper(pos: int) -> List[int]:
            ss = []
            div = nums[pos - 1] if pos > 0 else 1
            for i in range(pos, n):
                if nums[i] % div == 0:
                    tss = [nums[i]] + helper(i + 1)
                    if len(tss) > len(ss):
                        ss = tss
            return ss
        nums.sort()
        n = len(nums)
        return helper(0)