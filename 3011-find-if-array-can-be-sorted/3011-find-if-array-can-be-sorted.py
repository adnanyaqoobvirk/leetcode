class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        bit_counts = {num: num.bit_count() for num in nums}
        pmax, cmin, cmax = 0, nums[0], nums[0]
        for num in nums:
            if bit_counts[num] != bit_counts[cmin]:
                if pmax > cmin:
                    return False
                pmax, cmin, cmax = cmax, num, num
            else:
                cmin, cmax = min(cmin, num), max(cmax, num)
        return pmax <= cmin