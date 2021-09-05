class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in range(0, k):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
            
        ans = [len(counts)]
        for i in range(1, len(nums) - k + 1):
            left, right = nums[i - 1], nums[i + k - 1]
            if counts[left] == 1:
                del counts[left]
            else:
                counts[left] -= 1
            counts[right] = counts.get(right, 0) + 1
            ans.append(len(counts))
            
        return ans