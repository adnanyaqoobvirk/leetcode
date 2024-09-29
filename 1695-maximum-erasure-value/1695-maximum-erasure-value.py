class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        score = 0
        max_score = 0
        l = 0
        for r in range(len(nums)):
            score += nums[r]

            while l < r and nums[r] in seen:
                score -= nums[l]
                seen.remove(nums[l])
                l += 1
            
            seen.add(nums[r])
            
            max_score = max(max_score, score)
        return max_score
            