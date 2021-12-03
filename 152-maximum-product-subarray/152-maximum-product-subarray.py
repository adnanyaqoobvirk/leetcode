class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, ans = len(nums) - 1, float('-inf')
        prefix_product = postfix_product = 1
        for i in range(n + 1):
            prefix_product *= nums[i]
            postfix_product *= nums[n - i]
            ans = max(ans, prefix_product, postfix_product)
            if not prefix_product:
                prefix_product = 1
            if not postfix_product:
                postfix_product = 1
        return ans
            