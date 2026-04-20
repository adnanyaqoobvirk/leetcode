class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        min_values = [inf] * (n + 1)
        min_value = inf
        for i in reversed(range(n)):
            min_value = min(min_value, nums[i])
            min_values[i] = min_value

        ans = []
        max_value = 0
        prev_idx = -1
        for i, num in enumerate(chain(nums, [inf])):
            if min_values[i] >= max_value:
                for j in range(prev_idx + 1, i):
                    ans.append(max_value)
                prev_idx = i - 1
            max_value = max(max_value, num)
        
        return ans