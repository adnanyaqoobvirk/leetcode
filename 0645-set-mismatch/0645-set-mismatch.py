class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        possible = {i for i in range(1, len(nums) + 1)}
        ans = []
        for num in nums:
            if num in possible:
                possible.remove(num)
            else:
                ans.append(num)
        ans.append(possible.pop())
        return ans