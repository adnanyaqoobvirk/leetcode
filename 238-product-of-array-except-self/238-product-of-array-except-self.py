class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lprefix = []
        product = 1
        for num in nums:
            product *= num
            lprefix.append(product)
            
        rprefix = []
        product = 1
        for num in reversed(nums):
            product *= num
            rprefix.append(product)
            
        ans = []
        for i in range(len(nums)):
            product = 1
            if i - 1 >= 0:
                product *= lprefix[i - 1]
            
            if len(nums) - i - 2 >= 0:
                product *= rprefix[len(nums) - i - 2]
            ans.append(product)
        return ans