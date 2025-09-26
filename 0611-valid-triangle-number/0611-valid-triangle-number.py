class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n < 3:
            return 0

        nums.sort()
        
        triplets = 0
        for i in range(n):
            k = i + 2
            for j in range(i + 1, n):
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                triplets += k - j - 1
        return triplets