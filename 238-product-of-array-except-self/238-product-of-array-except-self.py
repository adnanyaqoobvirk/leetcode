class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        product = 1
        for num in nums:
            product *= num
            ans.append(product)
            
        product = 1
        for i in reversed(range(len(nums))):
            ans[i] = (product * ans[i - 1]) if i - 1 >= 0 else product
            product *= nums[i]
        return ans