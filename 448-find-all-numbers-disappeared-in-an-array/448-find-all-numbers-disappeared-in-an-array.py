class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        ans = []
        for num in range(1, len(nums) + 1):
            if num not in seen:
                ans.append(num)
        return ans