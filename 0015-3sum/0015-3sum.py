class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        num_indices = {}
        for i, num in enumerate(nums):
            num_indices[num] = i
        
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n):
                total = -1 * (nums[i] + nums[j])
                if total in num_indices and num_indices[total] > j:
                    ans.append([nums[i], nums[j], total])
        return ans