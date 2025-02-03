class Solution:
    def check(self, nums: List[int]) -> bool:
        rpos = -1
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                rpos = i
                break
        if rpos == -1:
            return True
        for i in range(rpos + 1, rpos + n):
            j = i % n
            if nums[j - 1] > nums[j]:
                return False
        return True