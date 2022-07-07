class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(left: int, right: int) -> int:
            if left > right:
                return -inf
            
            mid = left + (right - left) // 2
            
            best_left_sum = curr = 0
            for i in reversed(range(left, mid)):
                curr += nums[i]
                best_left_sum = max(curr, best_left_sum)

            best_right_sum = curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(curr, best_right_sum)
                
            left_max = helper(left, mid - 1)
            right_max = helper(mid + 1, right)
            
            return max(
                left_max,
                right_max,
                best_left_sum + nums[mid] + best_right_sum
            )
        return helper(0, len(nums) - 1)