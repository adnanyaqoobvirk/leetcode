class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        bit_counts = {num: num.bit_count() for num in nums}
        pseg, cseg = [], [nums[0]]
        for i in range(1, len(nums)):
            if bit_counts[nums[i]] != bit_counts[cseg[0]]:
                cseg.sort()
                if pseg and pseg[-1] > cseg[0]:
                    return False
                pseg, cseg = cseg, []
            cseg.append(nums[i])
        cseg.sort()
        return not pseg or pseg[-1] <= cseg[0]