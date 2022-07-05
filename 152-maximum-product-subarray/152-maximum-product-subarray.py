class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        @cache
        def maxp(pos: int, start: bool) -> int:
            if pos == n:
                return 1 if start else -inf
            
            if start:
                return max(
                    nums[pos] * (
                        minp(pos + 1) if nums[pos] < 0 else maxp(pos + 1, True)
                    ),
                    1
                )
            else:
                return max(
                    nums[pos] * (
                        minp(pos + 1) if nums[pos] < 0 else maxp(pos + 1, True)
                    ),
                    maxp(pos + 1, False)
                )
        @cache
        def minp(pos: int) -> int:
            if pos == n:
                return 1
            
            if nums[pos] < 0:
                return nums[pos] * maxp(pos + 1, True)
            else:
                return nums[pos] * minp(pos + 1)
            
        n = len(nums)
        return maxp(0, False)