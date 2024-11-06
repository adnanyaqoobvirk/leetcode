class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        pmax = cmax = cbits = 0
        for num in nums:
            if num.bit_count() != cbits:
                pmax, cmax, cbits = cmax, 0, num.bit_count()
            if pmax > num:
                return False
            cmax = max(cmax, num)
        return True