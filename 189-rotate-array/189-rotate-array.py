class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        tmp = [0] * n
        for i in range(n - k):
            tmp[i + k] = nums[i]
        
        for i in range(k):
            tmp[i] = nums[n - k + i]
        
        for i, num in enumerate(tmp):
            nums[i] = num
        
            