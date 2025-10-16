class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        rcounts = defaultdict(int)
        for num in nums:
            rcounts[num % value] += 1
        
        min_count = len(nums)
        for r in range(value):
            min_count = min(min_count, rcounts[r])
        
        max_mex = min_count * value
        for r in range(value):
            if rcounts[r] - min_count > 0:
                max_mex += 1
            else:
                break
        return max_mex